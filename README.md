
# 📺 StreamSight - OTT Analytics & Machine Learning

StreamSight is an end-to-end OTT analytics project that combines **MySQL, SQL, Python, Power BI, and Machine Learning** to analyze user engagement, content performance, and watch-time patterns on a streaming platform.

The project includes an interactive Power BI dashboard and a machine learning pipeline for comparing actual and predicted watch duration.

---

## 📌 Project Overview

Streaming platforms generate large amounts of user engagement data. StreamSight analyzes this data to identify viewing trends, understand user behavior, evaluate content performance, and explore machine learning-based watch-time prediction.

The project follows a complete analytics workflow:

1. Dataset generation and preparation
2. SQL-based data analysis
3. Python data processing
4. Machine Learning model training
5. Power BI dashboard development
6. Model evaluation and prediction analysis

---

## 🚀 Key Features

### 📊 SQL Analytics

- Overall platform KPIs
- Genre-wise watch-time analysis
- Subscription plan analysis
- Top 10 most-watched shows
- Monthly watch-time trends
- Average watch time per user
- City-wise watch-time analysis
- Movie vs. series comparison
- Data quality checks

### 📈 Power BI Dashboard

- Total users and total shows
- Total watch records
- Total watch time
- Average watch duration
- Watch time by genre
- Watch time by city
- Monthly watch-time trends
- Top 5 most-watched shows
- Users by subscription plan
- Interactive subscription and genre slicers

### 🤖 Machine Learning

- Random Forest Regressor for watch-time prediction
- Actual vs. predicted watch-time comparison
- Genre-wise prediction visualization
- Show-level prediction insights
- Model evaluation using MAE and R² Score

---

## 🧠 Machine Learning Implementation

### Model Used

**Random Forest Regressor**

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to generate predictions.

For this project, the model was used to explore whether available user and content-related information could help predict watch duration.

### ML Workflow

1. Load watch-history data from MySQL.
2. Join watch-history data with user and show information.
3. Prepare the dataset for machine learning.
4. Separate input features and the target variable.
5. Split the dataset into training and testing sets.
6. Train the Random Forest Regressor.
7. Generate predictions on the test dataset.
8. Evaluate the model using MAE and R² Score.
9. Export predictions to a CSV file.
10. Import the predictions into Power BI for visualization.

### Target Variable

`watch_minutes`

The model attempts to predict the watch duration associated with a viewing record.

### Prediction Output

The generated predictions are saved in:

```text
data/ml_predictions.csv
```

The output is used in Power BI to compare actual and predicted watch duration.

---

## 📏 Model Evaluation Results

The Random Forest Regressor was evaluated on the test dataset using Mean Absolute Error and R² Score.

| Evaluation Metric | Result |
|---|---:|
| Model | Random Forest Regressor |
| Dataset Size | 3,000 watch records |
| Mean Absolute Error (MAE) | 45.72 minutes |
| R² Score | -0.12 |

### Understanding the Results

**Mean Absolute Error (MAE): 45.72 minutes**

The model's average absolute prediction error on the evaluated test set was approximately 45.72 minutes.

A lower MAE generally indicates smaller prediction errors.

**R² Score: -0.12**

The negative R² Score indicates that the current model did not outperform a baseline that predicts the mean target value on the evaluated test set.

This result suggests that the current features and dataset are not sufficient for reliable watch-time prediction. Further feature engineering, improved data collection, and alternative target definitions would be required to improve the model.

> Note: The machine learning component is an exploratory prediction pipeline. The reported metrics should not be interpreted as evidence of production-ready predictive performance.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and machine learning |
| Pandas | Data manipulation and preparation |
| NumPy | Numerical operations |
| Scikit-learn | Random Forest model and evaluation |
| MySQL | Database management and SQL analysis |
| Power BI | Interactive dashboards and visualization |
| Git & GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
StreamSight/
│
├── data/
│   ├── users.csv
│   ├── shows.csv
│   ├── watch_history.csv
│   └── ml_predictions.csv
│
├── python/
│   ├── generate_dataset.py
│   ├── analyze_data.py
│   └── ml_model.py
│
├── sql/
│   └── analytics_queries.sql
│
├── StreamSight_OTT_Analytics.pbix
├── .gitignore
└── README.md
```

---

## 📊 Dashboard Pages

### 1. OTT Analytics Dashboard

The main dashboard provides insights into:

- User demographics and subscription plans
- Content genres and viewing behavior
- City-wise engagement
- Monthly watch-time trends
- Most-watched shows

### 2. Machine Learning Predictions

The ML dashboard includes:

- Actual average watch time
- Predicted average watch time
- Actual vs. predicted watch time by genre
- MAE and R² Score
- Genre-based filtering
- Show-level prediction insights
- Model information

---

## 🔄 End-to-End Workflow

```text
Data Generation
      |
      v
MySQL Database
      |
      v
SQL Analytics
      |
      v
Python Data Processing
      |
      v
Random Forest Regressor
      |
      v
Model Evaluation
      |
      v
ML Predictions CSV
      |
      v
Power BI Dashboard
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Samridh24/StreamSight-OTT-Analytics.git
```

```bash
cd StreamSight-OTT-Analytics
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn mysql-connector-python joblib
```

### 3. Configure MySQL

Create a MySQL database named:

```sql
CREATE DATABASE streamsight;
```

Ensure that the required tables are available:

- users
- shows
- watch_history

Update the database connection configuration in the Python scripts as required.

### 4. Run the ML Pipeline

```bash
python python/ml_model.py
```

The script trains the model and generates the prediction file:

```text
data/ml_predictions.csv
```

### 5. Open the Power BI Dashboard

Open:

```text
StreamSight_OTT_Analytics.pbix
```

Refresh the data sources if required.

---

## 🔮 Future Improvements

- Collect a larger and more representative viewing dataset
- Add user engagement and session-level features
- Explore watch-time prediction using more suitable historical features
- Compare Random Forest with Linear Regression and other regression models
- Perform cross-validation and hyperparameter tuning
- Introduce classification models for user churn prediction
- Add automated data refresh
- Deploy the dashboard and ML pipeline for regular monitoring

---

## 🎯 Learning Outcomes

- Developed SQL queries for business-oriented data analysis
- Created interactive dashboards using Power BI
- Performed data preparation using Python and Pandas
- Implemented a Random Forest regression pipeline
- Evaluated machine learning predictions using MAE and R² Score
- Integrated analytical and machine learning outputs into a single project

---

## 👨‍💻 Author

**Samridh Sagar**

GitHub: [Samridh24](https://github.com/Samridh24)
