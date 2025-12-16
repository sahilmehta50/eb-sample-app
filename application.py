from flask import Flask

application = Flask(__name__)

@application.get("/")
def home():
    return "Deployed from GitHub Actions ✅ EB Green"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
