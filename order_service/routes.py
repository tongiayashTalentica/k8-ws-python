from flask import Blueprint, request
from service import place_order

order_bp = Blueprint('order', __name__)

@order_bp.route('/place', methods=['GET'])
def place_order_route():
    coffee_type = request.args.get('coffeeType', 'cappuccino')
    quantity = int(request.args.get('quantity', '1'))
    return place_order(coffee_type, quantity)