from flask import Blueprint, request, jsonify

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/stock', methods=['GET'])
def get_stock():
    # Dummy response
    return jsonify({
        "espressoShot": {"name": "Espresso Shot", "quantity": 10},
        "milk": {"name": "Milk", "quantity": 1000},
        "hotWater": {"name": "Hot Water", "quantity": 99999999},
        "milkFoam": {"name": "Milk Foam", "quantity": 500}
    })

@inventory_bp.route('/used', methods=['POST'])
def use_ingredient():
    ingredients = request.json
    available = True
    for ingredient, quantity in ingredients.items():
        if quantity > 10:  # Dummy check
            available = False
            break
    if available:
        for ingredient, quantity in ingredients.items():
            # Dummy update
            pass
    return jsonify({"available": available})