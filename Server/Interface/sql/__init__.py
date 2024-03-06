from .check_auth_db import check_auth
from .check_permissions_db import check_permission
from .create_auth_db import create_auth_database
from .create_permissions_db import create_permissions_database
from .insert_auth_db import insert_into_auth
from .insert_permissions_db import insert_into_permissions
import os

class AuthDB:
    def __init__(self):
        if not os.path.exists('auth.db'):
            create_auth_database()

    def check_auth(self, userid, mac_address, ip_address, hash_value):
        return check_auth(userid, mac_address, ip_address, hash_value)

    def insert_into_auth(self, userid, mac_address, ip_address, hash_value):
        return insert_into_auth(userid, mac_address, ip_address, hash_value)

class PermissionsDB:
    def __init__(self):
        if not os.path.exists('auth.db'):
            create_permissions_database()

    def check_permission(self, userid, mac_address, ip_address, permission):
        return check_permission(userid, mac_address, ip_address, permission)

    def insert_into_permissions(self, userid, mac_address, ip_address, shutdown_servers, restart_servers, view_metrics):
        return insert_into_permissions(userid, mac_address, ip_address, shutdown_servers, restart_servers, view_metrics)
