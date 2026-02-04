import streamlit as st
import pandas as pd
import pickle

# -----------------------------------------------------------------------------
# Load Model
# -----------------------------------------------------------------------------
@st.cache_resource
def load_model():
    with open("best_customer_spend_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -----------------------------------------------------------------------------
# App UI
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Customer Spend Prediction", layout="centered")

st.title("💰 Customer Spend Prediction (Next 30 Days)")
st.write("Enter customer details below to predict next 30 days spend.")

# -----------------------------------------------------------------------------
# Input Fields
# -----------------------------------------------------------------------------
with st.form("prediction_form"):
    total_spend = st.number_input("Total Spend", value=5200.50)
    total_transactions = st.number_input("Total Transactions", value=45, step=1)
    avg_order_value = st.number_input("Avg Order Value", value=115.50)

    recency_days = st.number_input("Recency Days", value=4, step=1)
    tenure_days = st.number_input("Tenure Days", value=730, step=1)

    spend_last_30d = st.number_input("Spend Last 30 Days", value=450.00)
    tx_last_30d = st.number_input("Transactions Last 30 Days", value=4, step=1)

    spend_last_60d = st.number_input("Spend Last 60 Days", value=950.00)
    tx_last_60d = st.number_input("Transactions Last 60 Days", value=9, step=1)

    spend_last_90d = st.number_input("Spend Last 90 Days", value=1400.00)
    tx_last_90d = st.number_input("Transactions Last 90 Days", value=12, step=1)

    unique_products = st.number_input("Unique Products", value=20, step=1)
    unique_categories = st.number_input("Unique Categories", value=5, step=1)

    dominant_category = st.selectbox(
        "Dominant Category",
        ["Electronics", "Fashion", "Grocery", "Home", "Other"]
    )

    segment_id = st.selectbox(
        "Customer Segment",
        ["VIP", "Regular", "Occasional"]
    )

    loyalty_status = st.selectbox(
        "Loyalty Status",
        ["Gold", "Silver", "Bronze", "None"]
    )

    total_loyalty_points = st.number_input("Total Loyalty Points", value=2500, step=1)
    is_cold_start = st.selectbox("Cold Start Customer", [0, 1])

    submit = st.form_submit_button("🔮 Predict Spend")

# -----------------------------------------------------------------------------
# Prediction
# -----------------------------------------------------------------------------
if submit:
    input_data = pd.DataFrame([{
        "total_spend": total_spend,
        "total_transactions": total_transactions,
        "avg_order_value": avg_order_value,
        "recency_days": recency_days,
        "tenure_days": tenure_days,
        "spend_last_30d": spend_last_30d,
        "tx_last_30d": tx_last_30d,
        "spend_last_60d": spend_last_60d,
        "tx_last_60d": tx_last_60d,
        "spend_last_90d": spend_last_90d,
        "tx_last_90d": tx_last_90d,
        "unique_products": unique_products,
        "unique_categories": unique_categories,
        "dominant_category": dominant_category,
        "segment_id": segment_id,
        "loyalty_status": loyalty_status,
        "total_loyalty_points": total_loyalty_points,
        "is_cold_start": is_cold_start
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"💸 Predicted Spend (Next 30 Days): ₹ {prediction:,.2f}")
