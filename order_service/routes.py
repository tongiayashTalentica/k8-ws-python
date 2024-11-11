from flask import Blueprint, request, jsonify
import requests

order_bp = Blueprint('order', __name__)
inventory_url = "http://localhost:8082"

@order_bp.route('/place', methods=['GET'])
def place_order():
    coffee_type = request.args.get('coffeeType', 'cappuccino')
    quantity = int(request.args.get('quantity', '1'))
    ingredients = get_ingredient(coffee_type, quantity)
    response = requests.post(f"{inventory_url}/inventory/used", json=ingredients)
    available = response.json().get("available", False)
    if available:
        return jsonify({"coffeeType": coffee_type, "quantity": quantity, "status": "Confirmed"})
    else:
        return jsonify({"coffeeType": coffee_type, "quantity": quantity, "status": "Out of Stock"})

def get_ingredient(coffee_type, quantity):
    # Dummy data for ingredients
    coffees = {
        "cappuccino": {"espressoShot": 1, "milk": 200, "milkFoam": 50},
        "americano": {"espressoShot": 1, "hotWater": 150}
    }
    ingredients = coffees.get(coffee_type, {})
    return {k: v * quantity for k, v in ingredients.items()}