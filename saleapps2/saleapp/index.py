from flask import Flask, render_template, request, redirect
import dao

app = Flask(__name__)


@app.route("/")
def index():

    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q, cate_id)
    return render_template("index.html", products=products)
@app.route("/products/<int:id>")
def products_details(id):
    product = dao.load_product_by_id(id)
    print(product)
    return render_template("product-details.html", product = product)


@app.route("/login", methods=['get','post'])
def login_user():
    if request.method.__eq__('POST'):
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        if username.__eq__('admin') and password.__eq__('123'):
            return redirect('/')

    return render_template("login.html")


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)



