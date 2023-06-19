from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "69b3845e92cfbcc48679a63a48615837"

from app import routes
