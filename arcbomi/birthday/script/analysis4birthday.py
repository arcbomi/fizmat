import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np
import seaborn as sns

# Load CSV file
df = pd.read_csv('a.csv')

# Convert birthday column to datetime format
df['birthday'] = pd.to_datetime(df['birthday'], format='%m-%d')
df['month'] = df['birthday'].dt.month
df['day'] = df['birthday'].dt.day

def month_name(month_num):
    return calendar.month_name[month_num]

df['month_name'] = df['month'].apply(month_name)

# General statistics
num_students = len(df)
unique_classes = df['class'].nunique()

# Birthdays distribution
birthday_counts = df.groupby(['month', 'day']).size().unstack(fill_value=0)
most_common_birthday = df['birthday'].dt.strftime('%m-%d').value_counts().idxmax()

# Average birthdays per day
total_days = 365  # Considering a non-leap year
avg_birthdays_per_day = num_students / total_days

# Month-wise student count
month_counts = df['month_name'].value_counts()

# Class-wise student count
class_counts = df['class'].value_counts()

# Print analysis
print(f'Total Students: {num_students}')
print(f'Unique Classes: {unique_classes}')
print(f'Most Common Birthday: {most_common_birthday} with {df["birthday"].dt.strftime("%m-%d").value_counts().max()} students')
print(f'Average Birthdays per Day: {avg_birthdays_per_day:.2f}')
print('\nClass Distribution:')
print(class_counts)
print('\nMonth Distribution:')
print(month_counts)

# Plot birthday distribution as a friendly 2D calendar
fig, ax = plt.subplots(figsize=(12, 8))
birthday_matrix = np.zeros((12, 31))

for month in range(1, 13):
    for day in range(1, 32):
        if day in birthday_counts.columns and month in birthday_counts.index:
            birthday_matrix[month - 1, day - 1] = birthday_counts.loc[month, day]

sns.heatmap(birthday_matrix, cmap='coolwarm', annot=True, fmt='.0f', linewidths=0.5, cbar=True, ax=ax)
ax.set_xticks(np.arange(31) + 0.5)
ax.set_xticklabels(range(1, 32))
ax.set_yticks(np.arange(12) + 0.5)
ax.set_yticklabels([calendar.month_abbr[i] for i in range(1, 13)])
ax.set_xlabel("Day")
ax.set_ylabel("Month")
ax.set_title("Birthday Distribution (Friendly Calendar View)")
plt.show()

# Plot class distribution sorted by grade
class_counts = df['class'].value_counts()
class_counts = class_counts.sort_index(key=lambda x: x.str.extract('(\d+)')[0].astype(int))
plt.figure(figsize=(10, 5))
class_counts.plot(kind='bar', color='skyblue')
plt.axhline(y=class_counts.mean(), color='red', linestyle='--', label='Mean')
plt.title('Class Distribution')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Plot month-wise birthday distribution
month_counts = df['month'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
month_counts.plot(kind='bar', color='lightcoral')
plt.axhline(y=month_counts.mean(), color='red', linestyle='--', label='Mean')
plt.title('Month-wise Birthday Distribution')
plt.xlabel('Month')
plt.ylabel('Number of Students')
plt.xticks(ticks=range(12), labels=[calendar.month_abbr[i+1] for i in range(12)], rotation=45)
plt.legend()
plt.show()

