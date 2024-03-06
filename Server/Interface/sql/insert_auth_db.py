import sqlite3

def insert_into_auth(userid, mac_address, ip_address, hash_value):
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Insert values into AuthTable
    cursor.execute('''INSERT INTO AuthTable
                  (userid, mac_address, ip_address, hash)
                  VALUES (?, ?, ?, ?)''',
                  (userid, mac_address, ip_address, hash_value))
    conn.commit()

    conn.close()

# Example usage
if __name__ == "__main__":
    insert_into_auth(1, "00:11:22:33:44:55", "192.168.1.1", "some_hash_value")
