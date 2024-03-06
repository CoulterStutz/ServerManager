import sqlite3

def create_permissions_database():
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Create PermissionsTable if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS PermissionsTable
                  (userid INTEGER, mac_address TEXT, ip_address TEXT,
                  shutdown_servers INTEGER, restart_servers INTEGER, view_metrics INTEGER)''')
    conn.commit()

    conn.close()

# Example usage
if __name__ == "__main__":
    create_permissions_database()
