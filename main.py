from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>This website is hosted on Heroku with gunicorn!</h3>"


if __name__ == "__main__":
    app.run()