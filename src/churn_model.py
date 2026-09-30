import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def build_model():
    df = pd.read_csv("data/processed_customers.csv")

    target = "churned_flag"
    features = [
        "plan_type",
        "region",
        "industry",
        "acquisition_channel",
        "onboarding_completed",
        "logins_per_month",
        "sessions_per_month",
        "feature_usage_score",
        "support_tickets",
        "days_since_signup",
        "monthly_revenue",
    ]

    X = df[features]
    y = df[target]

    categorical_cols = ["plan_type", "region", "industry", "acquisition_channel"]
    numeric_cols = [c for c in features if c not in categorical_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numeric_cols),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(
                n_estimators=300,
                max_depth=8,
                min_samples_leaf=3,
                random_state=42
            )),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("AUC:", round(roc_auc_score(y_test, y_proba), 4))
    print(classification_report(y_test, y_pred))

    # Save the model
    with open("models/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save feature importance
    feature_importances = model.named_steps["classifier"].feature_importances_
    feature_names = model.named_steps["preprocessor"].get_feature_names_out()

    importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": feature_importances
    }).sort_values("importance", ascending=False)

    importance_df.to_csv("models/churn_feature_importance.csv", index=False)

    print("Model saved to models/churn_model.pkl")
    print("Feature importance saved to models/churn_feature_importance.csv")


if __name__ == "__main__":
    build_model()