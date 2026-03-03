import streamlit as st
import pandas as pd

companies = pd.read_csv("data/company_esg_financial_dataset.csv")
companies_cleaned = companies.drop(columns=["GrowthRate"])

st.write("""
# ESG Financial Dashboard
""")

means = companies_cleaned[["ESG_Overall", "MarketCap", "ProfitMargin"]].mean()
st.metric(label="Average ESG Score", value=means["ESG_Overall"].round(2))
st.metric(label="Average Market Capital", value=means["MarketCap"].round(2))
st.metric(label="Average Profit Margin", value=means["ProfitMargin"].round(2))

sector_mean = companies_cleaned.groupby("Industry")[["ESG_Overall"]].agg("mean")
st.bar_chart(sector_mean, sort=True)



