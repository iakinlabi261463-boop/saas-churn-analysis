-- Monthly churn rate
SELECT
  DATE_TRUNC('month', signup_date) AS signup_month,
  AVG(CASE WHEN churned_flag = 1 THEN 1.0 ELSE 0 END) * 100 AS churn_rate_pct
FROM customers
GROUP BY DATE_TRUNC('month', signup_date)
ORDER BY signup_month;

-- Churn by plan
SELECT
  plan_type,
  AVG(CASE WHEN churned_flag = 1 THEN 1.0 ELSE 0 END) * 100 AS churn_rate_pct,
  COUNT(*) AS customer_count
FROM customers
GROUP BY plan_type
ORDER BY churn_rate_pct DESC;

-- Retention after 1 month and 3 months
WITH cohorts AS (
  SELECT
    DATE_TRUNC('month', signup_date) AS cohort_month,
    customer_id
  FROM customers
)
SELECT
  cohort_month,
  COUNT(*) AS total_customers,
  COUNT(CASE WHEN churned_flag = 1 THEN 1 END) AS churned_customers
FROM customers
GROUP BY cohort_month
ORDER BY cohort_month;

-- Customers with onboarding not completed
SELECT
  onboarding_completed,
  AVG(CASE WHEN churned_flag = 1 THEN 1.0 ELSE 0 END) * 100 AS churn_rate_pct,
  COUNT(*) AS total_customers
FROM customers
GROUP BY onboarding_completed;

-- Low usage risk
SELECT
  plan_type,
  AVG(CASE WHEN feature_usage_score < 40 AND churned_flag = 1 THEN 1.0 ELSE 0 END) * 100 AS low_usage_churn_rate,
  COUNT(*) AS customer_count
FROM customers
GROUP BY plan_type;