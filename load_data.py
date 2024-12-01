import pandas as pd
import psycopg2

# Load the transformed data
df = pd.read_csv("transformed_data.csv")

# Database connection parameters
db_config = {
    'dbname': 'ml_pipeline',
    'user': 'postgres',
    'password': '123',  # Replace with your PostgreSQL password
    'host': 'localhost',
    'port': 5432
}

# Establish a connection to the database
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    print("Connected to the database!")

    # Create the table (if it doesn't exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title TEXT,
            body TEXT
        );
    """)
    conn.commit()

    # Insert the data into the table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO posts (title, body) VALUES (%s, %s)
        """, (row['title'], row['body']))

    conn.commit()
    print("Data loaded into the 'posts' table.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Database connection closed.")
