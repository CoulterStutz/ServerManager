import sqlite3

def create_auth_database():
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Create AuthTable if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS AuthTable
                  (userid INTEGER, mac_address TEXT, ip_address TEXT, hash TEXT)''')
    conn.commit()

    conn.close()

# Example usage
if __name__ == "__main__":
    create_auth_database()
