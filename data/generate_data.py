import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def generate_data(n_customers=5000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    today = datetime.today().date()
    start_date = today - timedelta(days=700)

    plans = ["Starter", "Growth", "Enterprise"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America"]
    industries = ["SaaS", "Retail", "Healthcare", "Finance", "Education", "Manufacturing"]
    channels = ["Organic", "Paid Search", "Referral", "Outbound Sales", "Partner"]

    customers = []

    for customer_id in range(1, n_customers + 1):
        signup_date = random_date(start_date, today)
        plan = np.random.choice(plans, p=[0.5, 0.35, 0.15])
        region = np.random.choice(regions)
        industry = np.random.choice(industries)
        acquisition_channel = np.random.choice(channels)

        # User behavior features
        days_since_signup = (today - signup_date).days
        onboarding_completed = int(np.random.random() < 0.75)
        logins = max(0, int(np.random.normal(45, 20)))
        sessions = max(0, int(np.random.normal(18, 8)))
        support_tickets = max(0, int(np.random.poisson(1.2)))
        feature_usage_score = max(0, min(100, int(np.random.normal(60, 20))))

        # churn probability based on behavior
        churn_score = (
            (0.25 if plan == "Starter" else 0.15 if plan == "Growth" else 0.05)
            + (0.12 if onboarding_completed == 0 else 0)
            + (0.18 if logins < 15 else 0)
            + (0.14 if sessions < 5 else 0)
            + (0.18 if feature_usage_score < 40 else 0)
            + (0.10 if support_tickets > 2 else 0)
            + (0.10 if acquisition_channel == "Paid Search" else 0)
            + (0.04 if region == "Latin America" else 0)
        )

        # adjust for older customer retention
        if days_since_signup > 180:
            churn_score += 0.08

        churn_prob = min(0.9, max(0.05, churn_score / 10))
        churned = int(np.random.random() < churn_prob)

        if churned:
            if days_since_signup >= 30:
                churn_days = random.randint(30, min(days_since_signup, 500))
            else:
                churn_days = days_since_signup

            churn_date = signup_date + timedelta(days=churn_days)
        else:
            churn_date = pd.NaT

        customers.append(
            {
                "customer_id": customer_id,
                "signup_date": signup_date,
                "plan_type": plan,
                "region": region,
                "industry": industry,
                "acquisition_channel": acquisition_channel,
                "onboarding_completed": onboarding_completed,
                "logins": logins,
                "sessions": sessions,
                "feature_usage_score": feature_usage_score,
                "support_tickets": support_tickets,
                "churned_flag": churned,
                "churn_date": pd.NaT if pd.isna(churn_date) else churn_date,
            }
        )

    customer_df = pd.DataFrame(customers)

    # Add revenue estimate
    plan_prices = {"Starter": 49, "Growth": 129, "Enterprise": 399}
    customer_df["monthly_revenue"] = customer_df["plan_type"].map(plan_prices)

    # Save files
    customer_df.to_csv("data/customers.csv", index=False)

    # Create a monthly activity file
    activity_records = []
    for _, row in customer_df.iterrows():
        months_active = max(1, min(24, int((today - row["signup_date"]).days / 30) + 1))
        for month in range(1, months_active + 1):
            month_date = row["signup_date"] + timedelta(days=30 * month)
            activity_records.append(
                {
                    "customer_id": row["customer_id"],
                    "month_date": month_date,
                    "logins": max(0, int(row["logins"] * (0.7 + np.random.random() * 0.6))),
                    "sessions": max(0, int(row["sessions"] * (0.6 + np.random.random() * 0.8))),
                    "feature_usage_score": max(
                        0,
                        min(
                            100,
                            int(row["feature_usage_score"] * (0.6 + np.random.random() * 0.8)),
                        ),
                    ),
                    "support_tickets": max(0, int(np.random.poisson(row["support_tickets"] / max(1, months_active)))),
                }
            )

    activity_df = pd.DataFrame(activity_records)
    activity_df.to_csv("data/user_activity.csv", index=False)

    return customer_df, activity_df


if __name__ == "__main__":
    generate_data()
    print("Synthetic SaaS dataset created in data/")