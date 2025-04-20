from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

def main():
    project_root = Path(__file__).parents[1]
    clean_csv    = project_root / "data" / "processed" / "cleaned.csv"
    df           = pd.read_csv(clean_csv, parse_dates=["Date"]).dropna(subset=["Date"])
    df.set_index("Date", inplace=True)

    series = df['New Price ($)'].asfreq("MS")

    fig_dir = project_root / 'reports' / 'figures'
    fig_dir.mkdir(parents=True,exist_ok=True)

    decomposition = seasonal_decompose(series, model='additive',period=12)
    fig = decomposition.plot()
    fig.set_size_inches(10,8)
    fig.savefig(fig_dir / 'decomposition_new_price.png', bbox_inches = 'tight')
    plt.close(fig)

    model = ARIMA(series, order=(1,1,1))
    fit = model.fit()

    horizon = 12
    forecast = fit.get_forecast(steps=horizon)
    fc_mean = forecast.predicted_mean
    fc_ci = forecast.conf_int()

    plt.figure()
    plt.plot(series.index, series, label='Observed')
    plt.plot(fc_mean.index, fc_mean, label='Forecast')
    plt.fill_between(
        fc_ci.index,
        fc_ci.iloc[:, 0],
        fc_ci.iloc[:, 1],
        alpha=0.3
    )
    plt.title("New Car Price: Observed & 12‑Month Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_dir / "forecast_new_price.png")
    plt.close()

    print(f"Time series decomposition and forecast saved to {fig_dir}")

if __name__ == "__main__":
    main()