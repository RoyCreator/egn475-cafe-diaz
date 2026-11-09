
# I import Flask so I can create my web application.
from flask import Flask

# I create my Flask application using this Python file.
app = Flask(__name__)

# This route tells Flask what to show on the homepage.
@app.route("/")

# This function runs when someone visits the homepage.
def home():

    # This sends a welcome message to the visitor.
    return "Welcome to Bewy Café"

# This route connects the /about URL to my about function.
@app.route("/about")

# This function runs when someone visits the about page.
def about():

    # This returns a short description of my café.
    return "Bewy Café is a coffee shop in Miami serving fresh coffee and pastries."

# This checks if I am running this Python file directly.
if __name__ == "__main__":

    # This starts my Flask application with debug mode enabled.
    app.run(debug=True)
