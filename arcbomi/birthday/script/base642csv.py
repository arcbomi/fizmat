import pandas as pd
import base64

# Read CSV file
df = pd.read_csv("student.csv")

# Function to decode name from UTF-8 Base64
def decode_base64(encoded_name):
    return base64.b64decode(encoded_name.encode("utf-8")).decode("utf-8")

# Apply decoding to 'name' column
df["name"] = df["name"].apply(decode_base64)

# Save the decoded CSV
df.to_csv("decoded_a.csv", index=False)

# Print the result
print(df)
