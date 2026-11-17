
# I import Flask so I can create my web application.
from flask import Flask, render_template, abort

# I create my Flask application using this Python file.
app = Flask(__name__)

# This route tells Flask what to show on the homepage.
@app.route("/")

# This function runs when someone visits the homepage.
def home():
    return render_template("index.html")

# This route connects the /about URL to my about function.
@app.route("/about")

# This function runs when someone visits the about page.
def about():

    # This returns a short description of my café.
    return "Bewy Café is a coffee shop in Miami serving fresh coffee and pastries."

# This checks if I am running this Python file directly.

@app.route("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)

@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next(
        (item for item in SAMPLE_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/order/new")
def new_order():
    return render_template("order.html", items=SAMPLE_ITEMS)


@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html", orders=SAMPLE_KITCHEN)


@app.route("/orders")
def orders():
    return render_template("orders.html", orders=SAMPLE_ORDERS)


if __name__ == "__main__":

    # This starts my Flask application with debug mode enabled.
    app.run(debug=True)

SAMPLE_ITEMS = [
    {"id": 1, "name": "Café con Leche", "category": "Coffee", "price_cents": 350},
    {"id": 2, "name": "Cortadito", "category": "Coffee", "price_cents": 275},
    {"id": 3, "name": "Colada", "category": "Coffee", "price_cents": 300},
    {"id": 4, "name": "Cuban Sandwich", "category": "Food", "price_cents": 950},
    {"id": 5, "name": "Guava Pastry", "category": "Pastries", "price_cents": 325},
    {"id": 6, "name": "Ham Croquette", "category": "Food", "price_cents": 225},
]    
    
SAMPLE_KITCHEN = [
    {"id": 101, "customer": "Maria", "item": "Café con Leche", "status": "Preparing"},
    {"id": 102, "customer": "Carlos", "item": "Cuban Sandwich", "status": "Pending"},
    {"id": 103, "customer": "Ana", "item": "Cortadito", "status": "Ready"},
]

SAMPLE_ORDERS = [
    {"id": 95, "customer": "Maria", "total_cents": 350, "status": "Completed"},
    {"id": 96, "customer": "Carlos", "total_cents": 950, "status": "Completed"},
    {"id": 97, "customer": "Ana", "total_cents": 600, "status": "Completed"},
]
