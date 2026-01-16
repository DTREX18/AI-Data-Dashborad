# Feature Documentation

## Core Features

### 1. Dataset Upload
- **Supported Formats**: CSV, XLSX
- **Maximum Size**: 50MB
- **Drag & Drop**: Full drag-and-drop support
- **Auto-Detection**: Automatic column type detection

### 2. Exploratory Data Analysis (EDA)
- **Summary Statistics**: Row/column counts, memory usage
- **Column Analysis**: Mean, median, std dev, unique values
- **Data Quality**: Missing value detection
- **Correlation Matrix**: Numeric column correlations
- **Outlier Detection**: IQR-based outlier identification
- **Data Types**: Automatic type inference

### 3. Predictive Analytics
- **Regression Models**:
  - Linear Regression
  - Random Forest Regressor
- **Classification Models**:
  - Random Forest Classifier
- **Metrics**:
  - R² Score, RMSE, MAE for regression
  - Accuracy, Precision, Recall for classification
- **Auto-Training**: Automatic model selection based on data

### 4. Time Series Forecasting
- **Methods**:
  - Prophet (with confidence intervals)
  - Exponential Smoothing (fallback)
- **Customizable Periods**: 1-60 periods ahead
- **Visualization**: Interactive forecast charts
- **Uncertainty**: Upper and lower confidence bounds

### 5. Risk Assessment
- **Anomaly Detection**: Isolation Forest algorithm
- **Risk Scoring**: 0-100 scale
- **Data Quality Score**: Overall dataset quality assessment
- **Contamination Rate**: Adjustable sensitivity
- **Anomaly Details**: Sample rows identified as anomalies

### 6. AI-Powered Insights
- **Chat Interface**: Ask questions about your data
- **OpenRouter Integration**: Multiple LLM models
- **Context-Aware**: Responses based on dataset summary
- **Real-Time Answers**: Instant AI-generated insights
- **Natural Language**: Natural language Q&A

### 7. Report Generation
- **Auto-Generated Reports**: AI-created summaries
- **Format Support**: HTML and PDF (extensible)
- **Content**:
  - Executive summary
  - Key findings
  - Risk assessment
  - Recommendations
- **Downloadable**: Direct download from dashboard

## Advanced Features

### Data Visualization
- **Charts**: Line, bar, pie, area charts
- **Interactive**: Hover tooltips, zoom, pan
- **Real-time**: Updates as you analyze
- **Responsive**: Works on all screen sizes

### Performance Optimization
- **Lazy Loading**: Data loads on-demand
- **Caching**: Repeated queries cached
- **Streaming**: Large file handling
- **Async Processing**: Non-blocking operations

### Security
- **File Validation**: Type and size checking
- **Data Privacy**: No external data storage (by default)
- **CORS**: Configurable cross-origin access
- **Error Handling**: Secure error messages

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Send chat message |
| Shift+Enter | New line in chat |
| Ctrl+U | Upload new dataset |
| Ctrl+S | Download report |

## API Rate Limits

- **File Upload**: 10 files/minute per session
- **Model Training**: 5 trainings/minute
- **AI Queries**: 30 queries/minute (OpenRouter limit)
- **Forecast**: 10 forecasts/minute

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## File Size Recommendations

- **Optimal**: < 10MB
- **Good**: < 50MB (maximum)
- **Columns**: < 100 columns recommended
- **Rows**: < 1,000,000 rows

## Data Type Support

| Type | EDA | Models | Forecast | Risk | AI |
|------|-----|--------|----------|------|-----|
| Numeric | ✓ | ✓ | ✓ | ✓ | ✓ |
| Categorical | ✓ | ✓ | ✗ | ✓ | ✓ |
| DateTime | ✓ | ✓ | ✓ | ✓ | ✓ |
| Text | ✓ | ✗ | ✗ | ✗ | ✓ |
