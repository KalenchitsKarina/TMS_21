from os import abort
from flask import Flask, render_template, request, redirect
from models import db, ProductModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create-page.html')

    if request.method == 'POST':
        product_id = request.form['product_id']
        name = request.form['name']
        url = request.form['url']
        price = request.form['price']
        amount = request.form['amount']
        comment = request.form['comment']
        product = ProductModel(product_id=product_id, name=name, url=url, price=price, amount=amount, comment=comment)
        db.session.add(product)
        db.session.commit()
        return redirect(f'/data/{product_id}')


@app.route('/data')
def retrieve_list():
    products = ProductModel.query.all()
    return render_template('data-list.html', products=products)


@app.route('/data/<int:id>')
def retrieve_single_product(id):
    product = ProductModel.query.filter_by(product_id=id).first()
    if product:
        return render_template('data.html', product=product)
    return f"Product with id = {id} doesn't exist"


@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    product = ProductModel.query.filter_by(product_id=id).first()
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit()
            name = request.form['name']
            url = request.form['url']
            price = request.form['price']
            amount = request.form['amount']
            comment = request.form['comment']
            product = ProductModel(product_id=id, name=name, url=url, price=price, amount=amount, comment=comment)
            db.session.add(product)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"

    return render_template('update.html', product=product)


@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    product = ProductModel.query.filter_by(product_id=id).first()
    if request.method == 'POST':
        if product:
            db.session.delete(product)
            db.session.commit()
            return redirect('/data')
        abort(404)

    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
