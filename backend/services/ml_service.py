import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score
from typing import Dict, Any, Tuple

class MLService:
    @staticmethod
    def train_regression_model(df: pd.DataFrame, target_col: str, model_type: str = "linear") -> Dict[str, Any]:
        """Train regression model"""
        # Prepare data
        X = df.drop(columns=[target_col]).select_dtypes(include=[np.number])
        y = df[target_col]
        
        # Remove rows with NaN
        mask = ~(X.isna().any(axis=1) | y.isna())
        X = X[mask]
        y = y[mask]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        if model_type == "linear":
            model = LinearRegression()
        else:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        mae = np.mean(np.abs(y_test - y_pred))
        
        return {
            "model_type": model_type,
            "target": target_col,
            "r_squared": float(r2),
            "rmse": float(rmse),
            "mae": float(mae),
            "samples_trained": len(X_train)
        }
    
    @staticmethod
    def train_classification_model(df: pd.DataFrame, target_col: str) -> Dict[str, Any]:
        """Train classification model"""
        X = df.drop(columns=[target_col]).select_dtypes(include=[np.number])
        y = df[target_col]
        
        mask = ~(X.isna().any(axis=1) | y.isna())
        X = X[mask]
        y = y[mask]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
        recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
        
        return {
            "model_type": "classification",
            "target": target_col,
            "accuracy": float(accuracy),
            "precision": float(precision),
            "recall": float(recall),
            "samples_trained": len(X_train)
        }
