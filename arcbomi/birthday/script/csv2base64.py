import pandas as pd
import base64

# Read CSV file
df = pd.read_csv("converted_a.csv")

# Function to encode name in UTF-8 Base64
def encode_base64(name):
    return base64.b64encode(name.encode("utf-8")).decode("utf-8")

# Apply encoding to 'name' column
df["name"] = df["name"].apply(encode_base64)

# Save the modified CSV
df.to_csv("encoded_a.csv", index=False)

# Print the result
print(df)
