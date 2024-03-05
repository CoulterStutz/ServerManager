from flask import Flask, jsonify, request
import sys
sys.path.append("/Data")
import Data

app = Flask(__name__)

class WebhookManager():
    def __init__(self):
        self.dm = Data.DataManager()
        self.data = {"message": "Initial message"}

    @app.route('/webhook')
    def webhook():
        self.update_data()
        return jsonify(self.data)

    @app.route('/shutdown')
    def shutdown():
        # Implement shutdown logic here
        return jsonify({"message": "Shutdown command sent"})

    def update_data(self):
        self.data = self.dm.return_data_json()

if __name__ == '__main__':
    app.run("0.0.0.0", port=5001)