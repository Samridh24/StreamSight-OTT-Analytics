
import pandas as pd

# --------------------------------
# READ DATASETS
# --------------------------------

# Read CSV files
users_df = pd.read_csv("data/users.csv")
shows_df = pd.read_csv("data/shows.csv")
watch_history_df = pd.read_csv("data/watch_history.csv")

# --------------------------------
# BASIC DATA INFORMATION
# --------------------------------

print("========== USERS DATA ==========")
print("Total users:", len(users_df))
print(users_df.head())

print("\n========== SHOWS DATA ==========")
print("Total shows:", len(shows_df))
print(shows_df.head())

print("\n========== WATCH HISTORY DATA ==========")
print("Total watch records:", len(watch_history_df))
print(watch_history_df.head())

# --------------------------------
# DATASET SHAPES
# --------------------------------

print("\n========== DATASET SHAPES ==========")

print("Users shape:", users_df.shape)
print("Shows shape:", shows_df.shape)
print("Watch history shape:", watch_history_df.shape)

print("\n========== CSV COLUMNS ==========")

print("Users columns:", users_df.columns.tolist())

print("Shows columns:", shows_df.columns.tolist())

print("Watch History columns:", watch_history_df.columns.tolist())