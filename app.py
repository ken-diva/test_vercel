from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/coba")
def coba():
    return "ini dari coba"


if __name__ == "__main__":
    app.run(debug=True)
