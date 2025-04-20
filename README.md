# 🚗 Auto Prices & Economic Trends (2019–2023)

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange)](https://streamlit.io/)  
[![SQLite](https://img.shields.io/badge/sqlite-DB-lightgrey)](https://www.sqlite.org/)  
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)  

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Tech Stack](#tech-stack)   
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation & Setup](#installation--setup)  
   - [Run the Analysis](#run-the-analysis)  
   - [Launch the Dashboard](#launch-the-dashboard)  
   - [Docker Deployment](#docker-deployment)  
4. [Key Insights](#key-insights)  
5. [3 Main Reports](#3-main-reports)  

---

## Project Overview

This end‑to‑end project demonstrates:

- **Data Ingestion & Cleaning** with Pandas  
- **Exploratory Data Analysis** (histograms, rolling averages, correlation matrices)  
- **SQL Analytics**: schema design, ETL into SQLite, analytical queries  
- **Time‑Series Modeling**: decomposition & ARIMA forecasting  
- **Interactive Dashboard** built in Streamlit & Plotly  
- **Reproducibility** via Docker and CI workflows  

All code, analyses, and artifacts are versioned here for easy reference.

---

## Tech Stack

- **Python 3.9+** – data manipulation, modeling, scripting  
- **Pandas & Matplotlib** – data wrangling & static plots  
- **SQLite** – relational database for ETL & queries  
- **Statsmodels** – time‑series decomposition & ARIMA forecasting  
- **Streamlit & Plotly** – interactive web dashboard  
- **Docker** – containerization for deployment  

## Getting Started

### Prerequisites
- Python 3.9 or newer
- Docker
- Git

### Installation & Setup
1. **Clone the repo**
```bash
git clone https://github.com/ryan-tobin/auto-prices-trend.git
cd auto-prices-trend
```
2. Create a virtual environment
```python
python -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```python
pip install pandas matplotlib statsmodels sqlite3 streamlit plotly
```

### Run The Analysis
1. Data Ingestion & Cleanup
```python
python notebooks/data_ingest_clean.py
```
2. Exploratory Data Analysis
```python
python notebooks/exploratory_analysis.py
```
3. SQL ETL & Queries
```python
python notebooks/sql_load.py
python notebooks/sql_analysis.py
```
4. Time Series Modeling & Forecast
```python
python notebooks/time_series_modeling.py
```

### Launch the Dashboard
```bash
streamlit run dashboard/app.py --server.address=0.0.0.0 --server.port=8501
```
- Then open your browser at http://localhost:8501.

### Docker Deployment
1. Build the image
```bash
docker build -t auto-prices-dashboard .
```
2. Run the Container
```bash
dockr run -p 8501:8501 auto-prices-dashboard
```
## Key Insights 
See reports/summary.md for detailed findings. Highlights include:
- Steady up-trend in average new car price (around $25,000 -> $33,000)
- Seasonality: winter dips & summer peaks
- COVID-era volatilit with sharp mid-2020 price spikes
- Forecast predicts continued growth into 2025 ($32,000-$36,000)

## 3 Main Reports
1. Rolling Avg. Prices
   
![Rolling Mean Prices](https://github.com/ryan-tobin/auto-prices-trend/blob/main/reports/figures/rolling_mean_prices.png)

2. Forecast Price
   
![Forecast](https://github.com/ryan-tobin/auto-prices-trend/blob/main/reports/figures/forecast_new_price.png)

3. Decomposition New Price
   
![Decomp New Price](https://github.com/ryan-tobin/auto-prices-trend/blob/main/reports/figures/decomposition_new_price.png)

