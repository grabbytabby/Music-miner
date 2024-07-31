import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(page_title="Mminer Dashboard", page_icon="⛏️", layout="wide")

# Title and description
st.title("Mminer Dashboard")
st.markdown("Welcome to the Mminer platform. Monitor your mining activities and token balance.")

# Sidebar
st.sidebar.header("User Info")
user_name = st.sidebar.text_input("Username")
user_balance = st.sidebar.number_input("Token Balance", min_value=0.0, format="%.2f")

# Main dashboard area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Mining Activity")
    
    # Simulated mining data
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    hash_rates = [100 + x * 2 for x in range(30)]  # Simulated increasing hash rate
    
    df = pd.DataFrame({"Date": dates, "Hash Rate (MH/s)": hash_rates})
    
    st.line_chart(df.set_index("Date"))

with col2:
    st.subheader("Token Distribution")
    
    # Simulated token distribution data
    distribution = {
        "Mining Rewards": 5000,
        "Staking": 3000,
        "Purchases": 1500,
        "Airdrops": 500
    }
    
    st.bar_chart(distribution)

# Mining control section
st.header("Mining Control")
col3, col4 = st.columns(2)

with col3:
    st.subheader("Start/Stop Mining")
    if st.button("Start Mining"):
        st.success("Mining started successfully!")
    if st.button("Stop Mining"):
        st.error("Mining stopped.")

with col4:
    st.subheader("Mining Pool")
    selected_pool = st.selectbox("Select Mining Pool", ["Pool A", "Pool B", "Pool C"])
    st.write(f"Currently mining with: {selected_pool}")

# Token transaction section
st.header("Token Transactions")
transaction_amount = st.number_input("Amount", min_value=0.0, format="%.2f")
recipient = st.text_input("Recipient Address")
if st.button("Send Tokens"):
    st.success(f"Successfully sent {transaction_amount} tokens to {recipient}")

# Footer
st.markdown("---")
st.markdown("© 2024 Mminer. All rights reserved.")
