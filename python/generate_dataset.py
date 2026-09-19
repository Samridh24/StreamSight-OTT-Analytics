
import pandas as pd
import numpy as np
from faker import Faker
from datetime import date, timedelta

# Faker object
fake = Faker()

# Reproducible random data
np.random.seed(42)

# Number of users
num_users = 500

# Age groups
age_groups = ["18-24", "25-34", "35-44", "45+"]

# Indian cities
cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Kolkata",
    "Noida"
]

# Subscription plans
subscription_plans = [
    "Free",
    "Basic",
    "Standard",
    "Premium"
]

# Generate user data
users = []

for i in range(1, num_users + 1):
    user = {
        "user_id": f"U{i:04d}",
        "age_group": np.random.choice(age_groups),
        "city": np.random.choice(cities),
        "subscription_plan": np.random.choice(
            subscription_plans,
            p=[0.40, 0.25, 0.20, 0.15]
        )
    }
    

    users.append(user)

# Convert list into DataFrame
users_df = pd.DataFrame(users)

# Save CSV file
users_df.to_csv("data/users.csv", index=False)

# Display results
print("Users dataset generated successfully!")
print("Total users:", len(users_df))
print("\nFirst 5 users:")
print(users_df.head())

print("\nSubscription distribution:")
print(users_df["subscription_plan"].value_counts())


# --------------------------------
# GENERATE SHOWS DATASET
# --------------------------------

# List of shows
show_names = [
    "The Last Signal",
    "Campus Days",
    "Dark Horizon",
    "City of Dreams",
    "The Hidden Truth",
    "Family Ties",
    "Code Warriors",
    "Midnight Stories",
    "The Final Mission",
    "Love in Delhi",
    "Beyond the Stars",
    "Crime Files",
    "The Startup",
    "Lost Memories",
    "House of Secrets",
    "The Last Kingdom",
    "Weekend Vibes",
    "Unknown Territory",
    "The Detective",
    "Life at 25",
    "The Great Journey",
    "Digital World",
    "Broken Promises",
    "The New Beginning",
    "Inside the Mind",
    "The Game Changer",
    "Mountain Tales",
    "The Silent Witness",
    "Future City",
    "One Last Chance"
]

genres = [
    "Thriller",
    "Comedy",
    "Drama",
    "Action",
    "Romance",
    "Documentary"
]

content_types = [
    "Movie",
    "Series"
]

# Generate show data
shows = []

for i, name in enumerate(show_names, start=1):
    show = {
        "show_id": f"S{i:03d}",
        "show_name": name,
        "genre": np.random.choice(genres),
        "content_type": np.random.choice(content_types)
    }

    shows.append(show)

# Convert into DataFrame
shows_df = pd.DataFrame(shows)

# Save CSV
shows_df.to_csv("data/shows.csv", index=False)

# Display results
print("\nShows dataset generated successfully!")
print("Total shows:", len(shows_df))

print("\nFirst 5 shows:")
print(shows_df.head())


# --------------------------------
# GENERATE WATCH HISTORY DATASET
# --------------------------------

# Number of watch history records
num_watch_records = 3000

# Generate watch history
watch_history = []

for i in range(1, num_watch_records + 1):

    # Select a random user and show
    selected_user = np.random.choice(users_df["user_id"])
    selected_show = np.random.choice(shows_df["show_id"])

    record = {
        "watch_id": f"W{i:05d}",
        "user_id": selected_user,
        "show_id": selected_show,
        "watch_minutes": np.random.randint(10, 181),
        "watch_date": fake.date_between(
    start_date=date.today() - timedelta(days=180),
    end_date=date.today()
)
    }

    watch_history.append(record)

# Convert list into DataFrame
watch_history_df = pd.DataFrame(watch_history)

# Save CSV file
watch_history_df.to_csv(
    "data/watch_history.csv",
    index=False
)

# Display results
print("\nWatch history dataset generated successfully!")
print("Total watch records:", len(watch_history_df))

print("\nFirst 5 watch records:")
print(watch_history_df.head())