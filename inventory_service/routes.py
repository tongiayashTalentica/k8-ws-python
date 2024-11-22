from flask import Blueprint
from service import get_stock, use_ingredient

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/stock', methods=['GET'])
def stock_route():
    return get_stock()

@inventory_bp.route('/used', methods=['POST'])
def use_ingredient_route():
    return use_ingredient()