#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]

    return bakeries, 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()

    bakery_dict = bakery.to_dict()

    return bakery_dict, 200

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods_by_price = BakedGood.query.order_by(BakedGood.price.desc()).all()
    bgbp_serialized = [good.to_dict() for good in baked_goods_by_price]

    return bgbp_serialized, 200

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good_by_price = BakedGood.query.order_by(BakedGood.price.desc()).first()
    bg_serialized = baked_good_by_price.to_dict()

    return bg_serialized, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
