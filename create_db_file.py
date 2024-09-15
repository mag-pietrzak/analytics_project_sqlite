import sqlite3

def create_empty_db(filename):
    # Connect to the SQLite database file (creates the file if it doesn't exist)
    conn = sqlite3.connect(filename)
    
    # Close the connection (optional, as it is closed automatically when the script ends)
    conn.close()

# Create an empty database file
create_empty_db('fake_online_shop.db')