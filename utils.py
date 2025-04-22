# utils.py
import io
import base64
import matplotlib.pyplot as plt
import io




def plot_forecast(df, forecast_df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['value'], label='Historical Data', marker='o')
    plt.plot(forecast_df['timestamp'], forecast_df['forecast_value'], label='Forecast', marker='x', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Forecast vs Historical')
    plt.legend()
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return f"data:image/png;base64,{plot_url}"
