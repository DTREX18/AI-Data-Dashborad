import pandas as pd
import numpy as np

try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False

from typing import Dict, Any

class ForecastService:
    @staticmethod
    def forecast_time_series(df: pd.DataFrame, date_col: str, value_col: str, periods: int = 12) -> Dict[str, Any]:
        """Forecast using time series data"""
        if not PROPHET_AVAILABLE:
            return {
                "error": "Prophet library not installed",
                "message": "Install with: pip install prophet"
            }
        
        # Prepare data for Prophet
        forecast_df = df[[date_col, value_col]].copy()
        forecast_df.columns = ['ds', 'y']
        forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])
        
        try:
            # Train model
            model = Prophet(daily_seasonality=False, yearly_seasonality=True)
            model.fit(forecast_df)
            
            # Make forecast
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)
            
            # Extract relevant columns
            forecast_data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
            
            return {
                "forecast": forecast_data[['ds', 'yhat']].to_dict('records'),
                "lower_bound": forecast_data['yhat_lower'].tolist(),
                "upper_bound": forecast_data['yhat_upper'].tolist(),
                "periods": periods
            }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def simple_forecast(df: pd.DataFrame, value_col: str, periods: int = 12) -> Dict[str, Any]:
        """Simple exponential smoothing forecast"""
        values = df[value_col].dropna().values
        
        if len(values) < 3:
            return {"error": "Insufficient data for forecasting"}
        
        # Simple exponential smoothing
        alpha = 0.3
        forecast = []
        last_value = values[-1]
        
        for _ in range(periods):
            last_value = alpha * last_value + (1 - alpha) * np.mean(values[-5:])
            forecast.append(last_value)
        
        return {
            "forecast": [{"value": v} for v in forecast],
            "method": "exponential_smoothing",
            "periods": periods
        }
