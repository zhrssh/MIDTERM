from flask import Flask
from flask import render_template

server = Flask(__name__)

@server.route("/login", methods=["GET"])
def main():
    return render_template("login.html")

@server.route("/register", methods=["GET"])
def register():
    return render_template("registration.html")

if __name__ == "__main__":
    server.run(host="0.0.0.0", port="8080")