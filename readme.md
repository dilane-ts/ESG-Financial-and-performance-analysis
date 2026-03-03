# Global ESG & Financial Performance Analysis Dashboard

## Description

This project explores the relationship between **Environmental, Social, and Governance (ESG) scores** and **financial performance metrics** for global companies. The analysis focuses on answering key business questions to guide sustainable investment decisions.  

The dataset contains:

- CompanyID, CompanyName, Industry, Region  
- Year, Revenue, ProfitMargin, MarketCap  
- ESG_Overall, ESG_Environmental, ESG_Social, ESG_Governance  
- CarbonEmissions, WaterUsage, EnergyConsumption  

The dashboard is built with **Python**, using **pandas**, **matplotlib**, **seaborn**, and **Streamlit** for interactive visualization.

---

## Business Questions Answered

1. **Which sectors have the best ESG performance?**  
   - The **Financial sector** has the **highest ESG scores**, while the **Transportation sector** has the **lowest scores**.  
   - Visualization: Bar chart comparing ESG scores by industry.  

2. **Is there a relationship between ESG score and profitability (ProfitMargin)?**  
   - The Pearson correlation between ProfitMargin and ESG score is **0.088**, indicating **no strong linear relationship**.  
   - Suggestion: Use **mutual information** or non-linear measures for further analysis.  
   - Visualization: Scatter plot ESG vs ProfitMargin.  

3. **Which regions combine high ESG scores with strong financial performance?**  
   - Europe shows the **highest average ESG scores**, whereas the Middle East has the **lowest**.  
   - Visualization: Pivot table and bar charts of ESG, ProfitMargin, and MarketCap by Region × Industry.  

4. **What are the top 10 companies by ESG and financial performance?**  
   - A top 10 ranking of companies was generated combining **ESG_Overall**, **ProfitMargin**, and **MarketCap**.  
   - Visualization: Table of top 10 companies and horizontal bar chart of ESG scores.

---

## Key Python Functions Used

- `groupby()`, `agg()`, `mean()`, `sum()`, `value_counts()`  
- `pivot_table()`  
- `sort_values()`, `nlargest()`  
- `apply()` / `cut()` for categorization  
- `matplotlib` & `seaborn` for visualizations  
- `Streamlit` for interactive dashboard

---

## Dashboard Structure

1. **Overview**  
   - Key metrics: ESG_Overall mean, ProfitMargin mean, MarketCap mean  

2. **ESG by Industry**  
   - Bar chart showing ESG_Overall per industry  

3. **ESG vs ProfitMargin**  
   - Scatter plot for potential correlation insights  

4. **Regional Analysis**  
   - Pivot table and bar charts for ESG_Overall, ProfitMargin, and MarketCap by Region × Industry  

5. **Top 10 Companies**  
   - Table and horizontal bar chart highlighting the best companies in ESG and financial performance  

---

## Insights

- ESG scores vary significantly by **sector** and **region**.  
- Financial performance (ProfitMargin) has little linear correlation with ESG score.  
- Europe leads in ESG performance, while the Middle East lags behind.  
- Top companies combine **high ESG** and **strong financial metrics**, making them models for sustainable investment.

---

## Dataset

- Source: [Kaggle – ESG and Financial Performance Dataset](https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset)  
- Single dataset with 15+ columns covering ESG, financial metrics, and environmental indicators

---

## How to Run

1. Clone this repository  
2. Install dependencies:  
```bash
pip install pandas matplotlib seaborn streamlit
streamlit run app.py
```

