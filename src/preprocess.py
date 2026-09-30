import pandas as pd


def load_data():
    customers = pd.read_csv("data/customers.csv")
    activity = pd.read_csv("data/user_activity.csv")

    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    customers["churn_date"] = pd.to_datetime(customers["churn_date"], errors="coerce")

    activity["month_date"] = pd.to_datetime(activity["month_date"])

    return customers, activity


def engineer_features(customers, activity):
    # Aggregate activity by customer
    activity_summary = (
        activity.groupby("customer_id", as_index=False)
        .agg(
            avg_logins=("logins", "mean"),
            avg_sessions=("sessions", "mean"),
            avg_feature_usage=("feature_usage_score", "mean"),
            total_support_tickets=("support_tickets", "sum"),
        )
    )

    df = customers.merge(activity_summary, on="customer_id", how="left")
    df["days_since_signup"] = (pd.Timestamp.today() - df["signup_date"]).dt.days
    df["logins_per_month"] = df["avg_logins"].fillna(0)
    df["sessions_per_month"] = df["avg_sessions"].fillna(0)
    df["feature_usage_score"] = df["avg_feature_usage"].fillna(0)
    df["support_tickets"] = df["total_support_tickets"].fillna(0)

    # Additional predictor features
    df["days_to_churn"] = (df["churn_date"] - df["signup_date"]).dt.days
    df["days_to_churn"] = df["days_to_churn"].fillna(df["days_since_signup"])

    # churned and not churned
    df["churned_flag"] = df["churned_flag"].astype(int)

    # Fill missing values
    df = df.fillna(0)

    return df


def main():
    customers, activity = load_data()
    df = engineer_features(customers, activity)

    # Save preprocessed dataset
    df.to_csv("data/processed_customers.csv", index=False)
    print("Processed dataset saved to data/processed_customers.csv")


if __name__ == "__main__":
    main()