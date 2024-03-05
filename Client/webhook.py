from flask import Flask, jsonify, request
import sys, time
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

        @self.app.route('/shutdown')


    def update_data(self):
        self.data = self.dm.return_data_json()
    def run(self):
        self.app.run("0.0.0.0", port=5001)