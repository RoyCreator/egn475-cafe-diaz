from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Bewy Café"

@app.route("/about")
def about():
    return "Bewy Café is a coffee shop in Miami serving fresh coffee and pastries."

if __name__ == "__main__":
    app.run(debug=True)