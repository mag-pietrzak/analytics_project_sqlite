import json
import sqlite3
import logging
import os
from generate_data import generate_data
from database_setup import create_database, Session 

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Defining extraction of data
"""
Extracts data from the specified tables in an SQLite database.

Parameters:
- database_url: str, path to the SQLite database file
- user_table_name: str, name of the user table
- product_table_name: str, name of the product table
- transaction_table_name: str, name of the transaction table

Returns:
- Tuple containing lists of records for user, product, and transaction tables.
"""
def extract_data(database_url, user_table_name, product_table_name, transaction_table_name):
    conn = None
    user_records = []
    product_records = []
    transaction_records = []

    logging.info("Extracting data...")

    try:
    # Connect to the SQLite database
        conn = sqlite3.connect(database_url)
        cursor = conn.cursor()

        # Extract data from User table
        try:
            cursor.execute(f"SELECT * FROM {user_table_name}")
            user_records = cursor.fetchall()
        except sqlite3.DatabaseError as e:
            logging.info(f"Error extracting data from {user_table_name}: {e}")

        # Extract data from Product table
        try:
            cursor.execute(f"SELECT * FROM {product_table_name}")
            product_records = cursor.fetchall()
        except sqlite3.DatabaseError as e:
            logging.info(f"Error extracting data from {product_table_name}: {e}")

        # Extract data from Transaction table
        try:
            cursor.execute(f"SELECT * FROM {transaction_table_name}")
            transaction_records = cursor.fetchall()
        except sqlite3.DatabaseError as e:
            logging.info(f"Error extracting data from {transaction_table_name}: {e}")

    except sqlite3.Error as e:
        logging.info(f"Database error: {e}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

    return user_records, product_records, transaction_records

# Defining saving files in JSON format
def save_files(user_records, product_records, transaction_records):
    """Prepares data for saving into JSON files."""
    user_data = [{"user_id": row[0], "first_name": row[1], "last_name": row[2], "address": row[3], "age": row[4], "email": row[5]} for row in user_records]
    product_data = [{"product_id": row[0], "product_name": row[1], "product_category": row[2],"product_type": row[3] , "product_price": row[4]} for row in product_records]
    transaction_data = [{"transaction_id": row[0], "user_id": row[1], "product_id": row[2], "transaction_date": row[3]} for row in transaction_records]

    """Saves data to a JSON file."""
    with open("user_records.json", "w") as user_file:
        json.dump(user_data, user_file, indent=4)

    with open("product_records.json", "w") as product_file:
        json.dump(product_data, product_file, indent=4)

    with open("transaction_records.json", "w") as transaction_file:
        json.dump(transaction_data, transaction_file, indent=4)

    logging.info("Files saved successfully.")

# Final generating of data and saving into JSON files
def main():
    if not os.path.exists('fake_online_shop.db'):
        logging.info("Database file does not exist. Creating new database.")
        engine = create_database()
        session = Session()
        generate_data()
    else:
        logging.info("Database file exists. Skipping creation.")

    database_url = 'fake_online_shop.db'
    user_table_name = 'Users'
    product_table_name = 'Products'
    transaction_table_name = 'Transactions'

    user_records, product_records, transaction_records = extract_data(database_url, user_table_name, product_table_name, transaction_table_name)
        # Proceed to save the extracted data to JSON files or perform further operations
    save_files(user_records, product_records, transaction_records)
    logging.info("Files saved successfully.")

if __name__ == "__main__":
    main()
