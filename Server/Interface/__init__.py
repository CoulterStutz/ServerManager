from flask import Flask
import flask

class WebInterface():
    def __init__(self) -> None:
        self.app = Flask(__name__)

        @self.app.route("/")
        def root():
            None
