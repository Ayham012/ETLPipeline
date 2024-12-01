import pandas as pd

# Load the extracted data
df = pd.read_csv("extracted_data.csv")

# Step 1: Keep only relevant columns
df = df[['title', 'body']]

# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Preprocess text (convert to lowercase)
df['title'] = df['title'].str.lower()
df['body'] = df['body'].str.lower()

# Save the transformed data to a new CSV
df.to_csv("transformed_data.csv", index=False)

print("Data transformation complete. Transformed data saved to 'transformed_data.csv'")
