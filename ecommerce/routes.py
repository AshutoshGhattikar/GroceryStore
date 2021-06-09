from ecommerce import app
from flask import render_template, request
from ecommerce.controllers.customer_controller import CustomerController
from ecommerce.controllers.category_controller import CategoryController

@app.route('/')
def home():
    top_3_categories = CategoryController().top_3_categories()
    return render_template('customer/home.html', showCarousel=True, response={'top_3_categories': top_3_categories})


@app.route('/about-us')
def about():
    return render_template('customer/about.html', title='About Us')


@app.route('/contact-us')
def contact():
    return render_template('customer/contact.html', title='Contact Us')


@app.route('/login', methods = ["POST"])
def login():
    User = request.form['Username']
    Pass = request.form['Password']

    client = pymongo.MongoClient("mongodb+srv://onlinegrocery2021iNeuron:onlinegrocery2021iNeuron@cluster0.xi9at.mongodb.net/OnlineGroceryDB?retryWrites=true&w=majority")
    db = client['OnlineGroceryDB']
    collection = db.User_details
    for record in collection.find({'User_id':User, 'password':Pass}):
        if len(record)==1:
            return render_template("home.html")
        else:
            return render_template("register.html")


@app.route('/register')
def register():
    return render_template('customer/auth/registration.html', title='Registration')


@app.route('/categories/<category>')
def categories(category):
    return render_template('customer/categories.html', title=category, showPageBanner=True)


@app.route('/products/<product>')
def products(product):
    return render_template('customer/products.html', title=product)


@app.route('/cart')
def cart():
    return render_template('customer/cart.html', title='Cart')


@app.route('/checkout')
def checkout():
    return render_template('customer/checkout.html', title='Checkout')


@app.route('/search')
def search():
    return render_template('customer/search.html', title='Search')
