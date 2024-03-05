import os

from flask import Flask, jsonify, request
import sys, time

from Client.config import AuthenticationSettings

sys.path.append("/Data")
import Data

class WebhookManager():
    def __init__(self):
        self.app = Flask(__name__)
        self.dm = Data.DataManager()
        self.data = {"message": "Initial message"}

        @self.app.route('/webhook')
        def webhook():
            self.update_data()
            return self.data

        @self.app.route('/shutdown', methods=['POST'])
        def shutdown():
            auth_header = request.headers.get('Authorization')
            if not auth_header or 'Basic ' not in auth_header:
                return jsonify({"error": "Unauthorized"}), 401

            auth_token = auth_header.split(' ')[1]
            username, password = auth_token.split(':')

            if username not in AuthenticationSettings['Users'] or AuthenticationSettings['Users'][username]['password'] != password:
                return jsonify({"error": "Unauthorized"}), 401

            if not AuthenticationSettings['Users'][username]['Permissions']['Shutdown']:
                return jsonify({"error": "Permission denied"}), 403

            os.system('shutdown /s /t 1')
            return jsonify({"message": "Shutting down"}), 200

    def update_data(self):
        self.data = self.dm.return_data_json()
    def run(self):
        self.app.run("0.0.0.0", port=5001)