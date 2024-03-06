import sqlite3

def insert_into_permissions(userid, mac_address, ip_address, shutdown_servers, restart_servers, view_metrics):
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Insert values into PermissionsTable
    cursor.execute('''INSERT INTO PermissionsTable
                  (userid, mac_address, ip_address, shutdown_servers, restart_servers, view_metrics)
                  VALUES (?, ?, ?, ?, ?, ?)''',
                  (userid, mac_address, ip_address, shutdown_servers, restart_servers, view_metrics))
    conn.commit()

    conn.close()

# Example usage
if __name__ == "__main__":
    insert_into_permissions(1, "00:11:22:33:44:55", "192.168.1.1", 1, 0, 1)
