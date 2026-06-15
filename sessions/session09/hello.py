from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Hello, Class!</h2>"

@app.route("/<name>")
def name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)




