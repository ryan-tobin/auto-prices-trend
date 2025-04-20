from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    project_root = Path(__file__).parents[1]
    clean_csv = project_root / "data" / "processed" / "cleaned.csv"
    df = pd.read_csv(clean_csv, parse_dates=['Date'])
    df = df.dropna(subset=['Date'])
    df.rename(
        columns={
            'Inflation Rate (%)': 'Inflation Rate',
            'Interest Rate (%)': 'Interest Rate'
        },
        inplace=True
    )

    df['Units Sold'] = (
        df['Units Sold']
        .astype(str)
        .str.replace(',','')
        .astype(float)
    )

    fig_dir = project_root / "reports" / "figures"
    fig_dir.mkdir(parents=True,exist_ok=True)

    plt.figure()
    df['New Price ($)'].hist(bins=20)
    plt.title("Distribution of New Car Prices")
    plt.xlabel('Price ($)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(fig_dir / "dist_new_price.png")
    plt.close()

    plt.figure()
    df['Used Price ($)'].hist(bins=20)
    plt.title("Distribution of Used Car Prices")
    plt.xlabel('Price ($)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(fig_dir / 'dist_used_price.png')
    plt.close()

    df.set_index('Date', inplace=True)
    df[['New Price ($)', 'Used Price ($)']].rolling('90D').mean().plot()
    plt.title('90 Day Rolling Avg. Price')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.savefig(fig_dir / 'rolling_mean_prices.png')
    plt.close()

    df['Year'] = df.index.year
    plt.figure()
    df.boxplot(column='New Price ($)', by='Year',grid=False)
    plt.title('New Car Price by Year')
    plt.suptitle('')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.savefig(fig_dir / 'boxplot_new_by_year.png')
    plt.close()

    corr = df[[
        'New Price ($)',
        'Used Price ($)',
        'Inflation Rate',
        'Interest Rate',
        'Units Sold'
    ]].corr()
    fig, ax = plt.subplots()
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    ticks = range(len(corr.columns))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(corr.columns, rotation=90)
    ax.set_yticklabels(corr.columns)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig(fig_dir / 'corr_matrix.png')
    plt.close()

    print(f"EDA plots saved to {fig_dir}")

if __name__ == "__main__":
    main()