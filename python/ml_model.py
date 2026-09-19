
import mysql.connector
import pandas as pd

from getpass import getpass
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. CONNECT TO MYSQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="streamsight"
)


# ==========================================
# 2. FETCH DATA
# ==========================================

query = """
SELECT
    wh.user_id,
    wh.show_id,
    wh.watch_date,
    wh.watch_minutes,
    u.subscription_plan,
    u.city,
    s.genre,
    s.content_type
FROM watch_history wh
JOIN users u
    ON wh.user_id = u.user_id
JOIN shows s
    ON wh.show_id = s.show_id;
"""

df = pd.read_sql(query, connection)

connection.close()

print("Data loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================

df["watch_date"] = pd.to_datetime(df["watch_date"])

df["watch_month"] = df["watch_date"].dt.month
df["watch_day_of_week"] = df["watch_date"].dt.dayofweek

df.drop("watch_date", axis=1, inplace=True)


# ==========================================
# 4. DEFINE FEATURES AND TARGET
# ==========================================

X = df.drop("watch_minutes", axis=1)
y = df["watch_minutes"]


# ==========================================
# 5. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 6. PREPROCESSING
# ==========================================

categorical_features = [
    "user_id",
    "show_id",
    "subscription_plan",
    "city",
    "genre",
    "content_type"
]

numeric_features = [
    "watch_month",
    "watch_day_of_week"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ==========================================
# 7. RANDOM FOREST MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ==========================================
# 8. TRAIN MODEL
# ==========================================

print("\nTraining model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# ==========================================
# 9. EVALUATE MODEL
# ==========================================

y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# ==========================================
# 10. GENERATE PREDICTIONS
# ==========================================

df["predicted_watch_minutes"] = pipeline.predict(X)


# ==========================================
# 11. SAVE PREDICTIONS FOR POWER BI
# ==========================================

output_columns = [
    "user_id",
    "show_id",
    "subscription_plan",
    "city",
    "genre",
    "content_type",
    "watch_month",
    "watch_day_of_week",
    "watch_minutes",
    "predicted_watch_minutes"
]

df[output_columns].to_csv(
    "data/ml_predictions.csv",
    index=False
)

print("\nPredictions saved successfully!")
print("File location: data/ml_predictions.csv")