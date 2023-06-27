import yfinance as yf
from datetime import timedelta
from prophet import Prophet


def predict(symbol: str, start_date: str, predict_days: int):

    # Get the stock data from yfinance
    new_df = yf.download(symbol, start=start_date, progress=False)
    new_data = new_df.filter(['Close'])
    new_dataset = new_data.values
    dates = new_df.index.to_list()
    
    df = new_df.reset_index()[["Date", "Close"]]
    df = df.rename({"Date": "ds", "Close": "y"}, axis=1)
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    
    future_dates = model.make_future_dataframe(periods=predict_days, freq='D')
    # Generate predictions for the future dates
    forecast = model.predict(future_dates)

    # Extract the predicted closing values for the next 60 days
    predicted_closing_values = forecast.tail(predict_days)["yhat"].values

    next_date = dates[-1]
    
    for _ in range(1, predict_days + 1):
        # Add 1 day to the current date and check if it's a weekend
        next_date += timedelta(days=1)
        while next_date.weekday() >= 5:
            next_date += timedelta(days=1)
        dates.append(next_date)
    
    return new_dataset, predicted_closing_values, dates