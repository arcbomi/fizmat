import pandas as pd

# Read the CSV file
df = pd.read_csv("a.csv")

# Function to truncate names
def truncate_name(name):
    return " ".join(name.split()[:2])

# Apply the function to the 'name' column
df["name"] = df["name"].apply(truncate_name)

# Save the modified CSV
df.to_csv("modified_a.csv", index=False)

# Display the result
print(df)
