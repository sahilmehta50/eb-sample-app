from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "<h1>EB + GitHub Actions SUCCESS ✅</h1>"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
