import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from typing import Dict, Any, List

class RiskService:
    @staticmethod
    def detect_anomalies(df: pd.DataFrame, contamination: float = 0.1) -> Dict[str, Any]:
        """Detect anomalies using Isolation Forest"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.empty:
            return {"anomalies": [], "risk_score": 0, "summary": "No numeric columns found"}
        
        # Handle missing values
        numeric_df = numeric_df.fillna(numeric_df.mean())
        
        # Train model
        iso_forest = IsolationForest(contamination=contamination, random_state=42)
        predictions = iso_forest.fit_predict(numeric_df)
        
        # Get anomaly indices
        anomaly_indices = np.where(predictions == -1)[0]
        
        anomalies = []
        for idx in anomaly_indices[:10]:  # Limit to 10
            anomaly_row = df.iloc[idx].to_dict()
            anomaly_row['row_index'] = int(idx)
            anomalies.append(anomaly_row)
        
        risk_score = len(anomaly_indices) / len(df) * 100  # Percentage
        
        return {
            "anomalies": anomalies,
            "total_anomalies": len(anomaly_indices),
            "risk_score": float(risk_score),
            "summary": f"Detected {len(anomaly_indices)} anomalies ({risk_score:.1f}% of data)"
        }
    
    @staticmethod
    def get_data_quality_score(df: pd.DataFrame) -> float:
        """Calculate data quality score (0-100)"""
        total_cells = df.shape[0] * df.shape[1]
        null_cells = df.isnull().sum().sum()
        
        quality_score = ((total_cells - null_cells) / total_cells * 100) if total_cells > 0 else 0
        return float(quality_score)
