# SaaS Customer Churn & Retention Analysis

[![Open Live Dashboard](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://saas-churn-analysis-9wrtueuznbvbjaqthexarv.streamlit.app/)

An end-to-end data analytics and machine learning project that analyzes SaaS customer churn, identifies retention drivers, and prioritizes customers at risk of cancellation.

## Live Dashboard

**[View the interactive Streamlit dashboard](https://saas-churn-analysis-9wrtueuznbvbjaqthexarv.streamlit.app/)**

## Project Overview

Customer churn is a major business challenge for subscription-based companies. This project examines customer behavior, product engagement, onboarding completion, support activity, and subscription information to identify patterns associated with churn.

The project combines:

- Exploratory data analysis
- SQL-based retention analysis
- Customer segmentation
- Feature engineering
- Machine learning
- Interactive dashboard development
- Business recommendations

## Business Questions

This project answers the following questions:

1. What is the overall customer churn rate?
2. Which plans and customer segments experience the highest churn?
3. Does onboarding completion affect retention?
4. How does product engagement relate to churn?
5. Which customer behaviors are associated with cancellation?
6. Which customers should receive proactive retention outreach?
7. What actions could help reduce customer churn?

## Key Features

### Customer churn analysis

Analyzes churn rates across:

- Subscription plans
- Regions
- Industries
- Acquisition channels
- Onboarding status

### Retention analysis

Examines customer retention patterns and cohort-level behavior based on signup timing and ongoing product activity.

### Churn risk modeling

Uses a Random Forest classification model to estimate churn risk based on:

- Product usage
- Login frequency
- Session activity
- Feature adoption
- Support ticket volume
- Onboarding completion
- Subscription plan
- Customer region
- Acquisition channel

### Interactive dashboard

The Streamlit dashboard includes:

- Churn rate KPI
- Average monthly revenue
- Total customer count
- Churn by subscription plan
- Churn by onboarding status
- Top churn drivers
- Customer risk summary

## Business Insights

The analysis is designed to identify patterns such as:

- Customers with low product engagement may be more likely to churn.
- Customers who do not complete onboarding may have higher cancellation risk.
- Customers with frequent support issues and low usage may require proactive outreach.
- Some acquisition channels and subscription plans may produce higher-risk customers.
- Customer retention strategies should focus on improving early product adoption.

> Note: The exact findings may change when the synthetic dataset is regenerated.

## Technology Stack

- **Python** — data processing and analysis
- **pandas** — data manipulation
- **NumPy** — numerical computing
- **scikit-learn** — machine learning
- **SQL** — retention and segmentation analysis
- **Matplotlib** — visualization
- **Seaborn** — statistical visualization
- **Streamlit** — interactive dashboard
- **GitHub** — version control and project hosting

## Project Structure

```text
saas-churn-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── generate_data.py
│   ├── customers.csv
│   ├── user_activity.csv
│   └── processed_customers.csv
├── sql/
│   └── retention_queries.sql
├── src/
│   ├── preprocess.py
│   └── churn_model.py
├── app/
│   └── dashboard.py
└── models/
    ├── churn_model.pkl
    └── churn_feature_importance.csv
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Isaiah-99/saas-churn-analysis.git
cd saas-churn-analysis
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the dataset

```bash
python data/generate_data.py
```

### 5. Prepare the modeling dataset

```bash
python src/preprocess.py
```

### 6. Train the churn model

```bash
python src/churn_model.py
```

### 7. Launch the dashboard

```bash
streamlit run app/dashboard.py
```

The dashboard will open at:

```text
http://localhost:8501
```

## Model Evaluation

The churn prediction model is evaluated using:

- Accuracy
- ROC-AUC
- Precision
- Recall
- F1-score
- Classification report

The model output includes estimated churn probabilities and feature importance rankings.

## Recommended Business Actions

Based on the types of patterns analyzed in this project, a SaaS company could:

1. Create onboarding campaigns for customers who have not completed setup.
2. Target low-engagement users with product education and usage reminders.
3. Prioritize customers with high support activity for customer success outreach.
4. Monitor churn risk by acquisition channel and subscription plan.
5. Use churn scores to prioritize retention resources.
6. Test personalized onboarding and product adoption campaigns.

## Important Assumptions and Limitations

This project uses a synthetic dataset created for portfolio and demonstration purposes.

Therefore:

- The data does not represent a real company.
- The churn relationships are simulated.
- Model performance should not be interpreted as production performance.
- Real-world deployment would require historical customer data.
- A production model would require monitoring, validation, and retraining.
- Correlation does not necessarily imply causation.

## Potential Improvements

Future improvements could include:

- Adding a real public SaaS dataset
- Building a true monthly cohort retention matrix
- Testing Logistic Regression, XGBoost, and LightGBM
- Using SHAP for model explainability
- Adding model calibration
- Creating automated data pipelines
- Adding unit tests
- Deploying with a production database
- Implementing customer-level churn alerts
- Designing retention experiments and A/B tests

## Portfolio Summary

> Built an end-to-end SaaS customer churn and retention analysis project using Python, SQL, machine learning, and Streamlit. Generated and analyzed synthetic customer behavior data, identified churn drivers, trained a Random Forest churn model, and developed an interactive dashboard to support customer retention decisions.

## Author

**Isaiah Akinlabi**

[GitHub Repository](https://github.com/Isaiah-99/saas-churn-analysis)  
[Live Dashboard](https://saas-churn-analysis-9wrtueuznbvbjaqthexarv.streamlit.app/)
