# 📡 Customer Retention AI: From Predictive Modeling to Blue Ocean Strategy

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)
![Strategy](https://img.shields.io/badge/Strategy-Blue%20Ocean-brightgreen.svg)

## Project Overview

This project addresses the challenge of customer churn in the telecommunications industry. Beyond simply predicting who will leave, this analysis integrates **Machine Learning** with business frameworks like **Blue Ocean Strategy** and **Lean Startup** to provide a proactive, high-value retention roadmap.

## Key Business Insights

Through a holistic Exploratory Data Analysis (EDA), I identified a **"Premium Friction"** pattern:

* **High-Value Risk:** Fiber optic customers exhibit the highest churn rates, especially when coupled with electronic check payments.
* **Support Gap:** A significant correlation exists between the absence of technical support and customer abandonment.
* **Financial Drivers:** Total and monthly charges are the strongest predictors of churn, indicating a need to increase perceived value rather than just cutting prices.

## Modeling & Optimization

I compared two distinct architectures to find the best balance between predictability and business utility:

1.  **Logistic Regression (Winner):** Emerged as the most effective model with a **Recall of 0.57**, successfully identifying the highest number of at-risk customers.
2.  **Random Forest:** Utilized for **Feature Importance** analysis, confirming that tenure and contract types are critical decision drivers.

> **Optimization Note:** I performed Hyperparameter Tuning using `RandomizedSearchCV`. Even after optimization, the Logistic Regression maintained superior Recall, proving that a robust linear model is best suited for the underlying patterns in this dataset.



## Strategic Recommendations (Blue Ocean)

To move the company away from "Red Ocean" price wars, I proposed:
* **AI-Powered 24/7 Support:** Automated troubleshooting via WhatsApp to bridge the support gap.
* **Value Bundles:** Specialized packages for Gamers and Remote Workers to justify premium pricing.
* **Experimental Framework:** An A/B Testing design to validate these interventions before full-scale deployment.

## Deployment Roadmap (MLOps)

The project includes a detailed plan for operationalization:
* **Architecture:** FastAPI containerized with Docker for real-time scoring.
* **Automation:** Integration with **n8n** to trigger retention playbooks based on real-time customer behavior.
* **Monitoring:** Drift detection and automated retraining cycles to ensure long-term model reliability.

The code and process in detail is in the repository.