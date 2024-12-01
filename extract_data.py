import requests
import pandas as pd

# Define the API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch data from the API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Extract JSON data from the response
    print("Data successfully fetched!")
else:
    print(f"Failed to fetch data. HTTP Status: {response.status_code}")

# Convert the JSON data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Save the data locally as a CSV file for later use
df.to_csv("extracted_data.csv", index=False)
print("Data saved to 'extracted_data.csv'")
