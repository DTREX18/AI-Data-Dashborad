import pandas as pd
import numpy as np
from typing import Dict, List, Any

class EDAService:
    @staticmethod
    def get_summary(df: pd.DataFrame) -> dict:
        """Generate EDA summary"""
        return {
            "row_count": len(df),
            "column_count": len(df.columns),
            "memory_usage": f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "numeric_summary": df.describe().to_dict()
        }
    
    @staticmethod
    def get_column_stats(df: pd.DataFrame) -> Dict[str, Any]:
        """Get statistics for each column"""
        stats = {}
        
        for col in df.columns:
            if df[col].dtype in ["int64", "float64"]:
                stats[col] = {
                    "type": "numeric",
                    "mean": float(df[col].mean()),
                    "median": float(df[col].median()),
                    "std": float(df[col].std()),
                    "min": float(df[col].min()),
                    "max": float(df[col].max()),
                    "q25": float(df[col].quantile(0.25)),
                    "q75": float(df[col].quantile(0.75))
                }
            else:
                stats[col] = {
                    "type": "categorical",
                    "unique": int(df[col].nunique()),
                    "mode": str(df[col].mode().values[0]) if len(df[col].mode()) > 0 else None
                }
        
        return stats
    
    @staticmethod
    def get_correlation_matrix(df: pd.DataFrame) -> dict:
        """Get correlation matrix for numeric columns"""
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.empty:
            return {}
        
        corr_matrix = numeric_df.corr()
        return corr_matrix.to_dict()
    
    @staticmethod
    def get_outliers(df: pd.DataFrame) -> Dict[str, List[int]]:
        """Detect outliers using IQR method"""
        outliers = {}
        
        for col in df.select_dtypes(include=[np.number]).columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            outlier_indices = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)].index.tolist()
            outliers[col] = outlier_indices
        
        return outliers
    
    @staticmethod
    def get_chart_data(df: pd.DataFrame) -> List[dict]:
        """Prepare data for charts"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        charts = []
        
        for col in numeric_cols[:5]:  # Limit to 5 columns
            chart_data = {
                "name": col,
                "type": "histogram",
                "data": df[col].value_counts().head(10).to_dict()
            }
            charts.append(chart_data)
        
        return charts
