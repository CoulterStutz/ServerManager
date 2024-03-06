import sqlite3

def check_permission(userid, mac_address, ip_address, permission):
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Check if mac_address and ip_address match the given userid
    cursor.execute('''SELECT mac_address, ip_address FROM AuthTable WHERE userid = ?''', (userid,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return -1
    stored_mac, stored_ip = row

    if stored_mac != mac_address or stored_ip != ip_address:
        conn.close()
        return -1

    # Check if the permission is set to true for the given userid
    cursor.execute(f'''SELECT {permission} FROM PermissionsTable WHERE userid = ?''', (userid,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return -1
    permission_value = row[0]

    conn.close()
    return 1 if permission_value else 0

# Example usage
if __name__ == "__main__":
    userid = 1
    mac_address = "00:11:22:33:44:55"
    ip_address = "192.168.1.1"
    permission = "shutdown_servers"
    result = check_permission(userid, mac_address, ip_address, permission)
    print(result)
