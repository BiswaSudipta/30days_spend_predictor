# 📈 Customer Lifetime Value (CLV) Prediction – End-to-End ML Pipeline

Predict **customer spending for the next 30 days** using real-world retail transaction data and a production-ready machine learning pipeline.

This project demonstrates **end-to-end data engineering, feature engineering, model training, evaluation, and deployment** using modern Python ML tooling.

---

## 🚀 Project Overview

**Goal:**
Predict how much a customer is likely to spend in the **next 30 days**, based on their historical behavior.

**Why it matters:**

* Helps businesses target high-value customers
* Enables smarter promotions and retention strategies
* Supports demand forecasting and revenue planning

This repository covers the **full ML lifecycle**, not just modeling.

---

## 🧠 Key Highlights

* ✔️ Realistic **synthetic data generation** (customers, transactions, products)
* ✔️ Robust **EDA & data quality checks**
* ✔️ Business-safe **data cleaning strategies**
* ✔️ Advanced **feature engineering (RFM, trends, momentum)**
* ✔️ Time-aware **30-day target creation (no data leakage)**
* ✔️ Gradient Boosting regression model
* ✔️ Full **FastAPI inference service**
* ✔️ **Streamlit-ready deployment**

---

## 🗂️ Repository Structure

```text
├── Datageneration&Eda.ipynb        # Data generation + EDA
├── Model_Building.ipynb            # Feature engineering + modeling
├── app.py                          # FastAPI inference API
├── best_customer_spend_model.pkl   # Trained ML pipeline
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
├── demo.png                        # Demo screenshot
└── LICENSE
```

---

## 🧾 Dataset Description

Synthetic retail data is generated to closely mimic real production systems:

### Tables Used

* **customer_details**
* **store_sales_header**
* **store_sales_line_items**
* **products**

### Data Characteristics

* Multiple transactions per customer
* Transaction → line-item hierarchy
* Temporal consistency enforced
* Intentional real-world issues (nulls, duplicates, outliers)

---

## 🔍 Exploratory Data Analysis (EDA)

Key checks performed:

* Row counts & schema validation
* Null value distribution
* Duplicate detection
* Date range validation
* Transaction consistency (header vs line items)
* Customer repeat behavior

📌 **Purpose:**
Identify data quality issues early and design robust cleaning rules.

---

## 🧹 Data Cleaning Strategy

Handled **real-world data problems** safely:

* Null values → business-aware imputation
* Duplicate records → deduplication using PKs
* Invalid foreign keys → removed safely
* Monetary mismatches → recomputed transaction totals
* Date issues → removed future or inconsistent dates
* Outliers → capped (not removed) to preserve high-value customers
* Cold-start customers → explicitly modeled

---

## 🧩 Feature Engineering

Customer-level features aggregated from historical data:

### Core Features

* Total spend
* Total transactions
* Average order value
* Recency & tenure

### Time-Window Features

* Spend & transactions (31–60 days)
* Spend & transactions (61–120 days)

### Advanced Features

* Spend velocity
* Transaction density
* Momentum ratios
* Loyalty efficiency
* Cold-start indicator

🎯 **Target Variable:**
`target_30d_spend` → Total spend in the **next 30 days**

---

## 🤖 Model Training

### Models Evaluated

* Baseline (Last 30-day spend)
* Linear Regression
* Gradient Boosting Regressor ✅

### Final Model

* **Gradient Boosting Regressor**
* Full preprocessing pipeline (imputation, scaling, encoding)
* Time-based train/validation split

### Metrics Used

* MAE
* RMSE
* R² Score

---

## 📦 Model Serialization

The **entire sklearn pipeline** (preprocessing + model) is saved using `joblib`:

```python
joblib.dump(model, "best_customer_spend_model.pkl")
```

This ensures **training-serving consistency** in production.

---

### Endpoints

* `GET /` → Health check
* `POST /predict` → Predict 30-day customer spend

### Features

* Model loaded safely at startup
* Strict input schema using Pydantic
* Handles unseen categorical values
* Ready for deployment

---

## 🌐 Streamlit Deployment

The model and API are designed to be **easily deployed using Streamlit** for interactive demos.

### Typical Streamlit Flow

* User inputs customer features
* Calls FastAPI `/predict` endpoint
* Displays predicted 30-day spend

📌 This makes the project **demo-ready for interviews and showcases**.

---

## 🖼️ Demo

Below is a sample demo of the application in action:

![Demo Screenshot](demo.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<biswasudipta>/<30days_spend_predictor>.git
cd <repo-name>
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run FastAPI

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---



---

## 🧠 Skills Demonstrated

* Data Engineering
* Feature Engineering
* Time-series aware ML
* Model evaluation
* Production best practices

---

## 📌 Future Improvements

* Add Docker support
* Deploy on cloud (Azure / AWS)
* Batch prediction endpoint
* Model monitoring & drift detection
* Experiment tracking (MLflow)

