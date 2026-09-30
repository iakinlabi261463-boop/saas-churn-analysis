import pickle

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SaaS Churn Dashboard", layout="wide")


@st.cache_data
def load_data():
    customers = pd.read_csv("data/customers.csv")
    processed = pd.read_csv("data/processed_customers.csv")
    feature_importance = pd.read_csv("models/churn_feature_importance.csv")
    return customers, processed, feature_importance


def main():
    customers, processed, feature_importance = load_data()

    st.title("SaaS Customer Churn Dashboard")

    # KPI cards
    churn_rate = customers["churned_flag"].mean() * 100
    avg_mrr = customers["monthly_revenue"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Churn Rate", f"{churn_rate:.2f}%")
    col2.metric("Average Monthly Revenue", f"${avg_mrr:,.2f}")
    col3.metric("Total Customers", f"{len(customers):,}")

    # Churn by plan
    st.subheader("Churn Rate by Plan")
    plan_churn = (
        customers.groupby("plan_type")["churned_flag"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    plan_churn.columns = ["plan_type", "churn_rate"]

    fig, ax = plt.subplots()
    sns.barplot(data=plan_churn, x="plan_type", y="churn_rate", palette="coolwarm", ax=ax)
    ax.set_ylabel("Churn rate")
    ax.set_xlabel("Plan type")
    st.pyplot(fig)

    # Churn by onboarding status
    st.subheader("Churn Rate by Onboarding Completion")
    onboarding = (
        customers.groupby("onboarding_completed")["churned_flag"]
        .mean()
        .reset_index()
    )
    onboarding.columns = ["onboarding_completed", "churn_rate"]
    fig2, ax2 = plt.subplots()
    sns.barplot(data=onboarding, x="onboarding_completed", y="churn_rate", palette="viridis", ax=ax2)
    ax2.set_xticklabels(["Not Completed", "Completed"])
    st.pyplot(fig2)

    # Risk feature importance
    st.subheader("Top Churn Drivers")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=feature_importance.head(10),
        x="importance",
        y="feature",
        palette="magma",
        ax=ax3
    )
    ax3.set_xlabel("Feature Importance")
    ax3.set_ylabel("")
    st.pyplot(fig3)

    # Segment table
    st.subheader("Customer Risk Summary")
    customers["risk_score"] = (
        (1 - processed["feature_usage_score"] / 100) * 100
        + processed["support_tickets"] * 6
        + (1 - processed["onboarding_completed"]) * 20
    )
    risk_summary = customers.assign(risk_score=customers["risk_score"]).sort_values("risk_score", ascending=False).head(20)
    st.dataframe(risk_summary[["customer_id", "plan_type", "region", "feature_usage_score", "support_tickets", "churned_flag", "risk_score"]])

    st.caption("This dashboard is a simplified view of customer churn drivers and risk segmentation.")


if __name__ == "__main__":
    main()