# SaaS Customer Churn & Retention Analysis

A data analysis and machine learning project designed to help a SaaS business understand why customers churn and identify the highest-risk accounts before they cancel.

## Business problem
Customer acquisition is expensive. When customers churn, the company loses recurring revenue and growth momentum. This project answers three questions:

1. Which customer segments churn the most?
2. What product behaviors are associated with churn?
3. Which customers are likely to churn in the next 30–90 days?

## Project goals
- Measure churn rate by segment
- Analyze cohort retention
- Identify churn drivers
- Build a churn risk model
- Recommend business actions

## Dataset
The project uses synthetic but realistic SaaS customer data generated in `data/generate_data.py`.

Features include:
- customer_id
- signup_date
- plan_type
- region
- industry
- acquisition_channel
- onboarding_completed
- logins
- sessions
- feature_usage_score
- support_tickets
- churned_flag
- churn_date

## Project pipeline
1. Generate synthetic customer and usage data
2. Clean and transform the data
3. Explore churn trends
4. Build a predictive churn model
5. Present results in a Streamlit dashboard

## Run the project

### 1. Install dependencies
```bash
pip install -r requirements.txt