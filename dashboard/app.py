import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/cleaned.csv',parse_dates=['Date'])
    return df

def main():
    st.title("🚗 Auto Prices & Economic Trends Dashboard")

    df = load_data()
    st.sidebar.subheader("Filter")
    date_min, date_max = st.sidebar.date_input(
        "Select Date Range",
        [df['Date'].min(), df['Date'].max()]
    )
    mask = (df['Date']>= pd.to_datetime(date_min)) & (df["Date"] <= pd.to_datetime(date_max))
    df = df.loc[mask]

    fig1 = px.line(
        df,
        x="Date",
        y=["New Price ($)", "Used Price ($)"],
        labels={"value": "Price ($)", "variable": "Type"},
        title="New & Used Car Prices Over Time"
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(
        df,
        x="Inflation Rate (%)",
        y="New Price ($)",
        trendline="ols",
        title="New Price vs Inflation Rate"
    )
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.scatter(
        df,
        x="Interest Rate (%)",
        y="New Price ($)",
        trendline="ols",
        title="New Price vs Interest Rate"
    )
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.bar(
        df,
        x="Date",
        y="Units Sold",
        title="Units Sold Over Time"
    )
    st.plotly_chart(fig4, use_container_width=True)

if __name__ == "__main__":
    main()