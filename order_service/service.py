import os
import requests
from flask import jsonify

def get_ingredient(coffee_type, quantity):
    # Read quantities from environment variables
    ESPRESSO_SHOT_QUANTITY = int(os.getenv('ESPRESSO_SHOT_QUANTITY', 0))
    MILK_QUANTITY = int(os.getenv('MILK_QUANTITY', 0))
    HOT_WATER_QUANTITY = int(os.getenv('HOT_WATER_QUANTITY', 0))
    MILK_FOAM_QUANTITY = int(os.getenv('MILK_FOAM_QUANTITY', 0))

    coffees = {
        "cappuccino": {"espressoShot": 1, "milk": 1, "milkFoam": 1},
        "americano": {"espressoShot": 1, "hotWater": 1}
    }
    ingredients = coffees.get(coffee_type, {})
    return {k: v * quantity for k, v in ingredients.items()}

def place_order(coffee_type, quantity):
    inventory_url = "http://localhost:8082"
    ingredients = get_ingredient(coffee_type, quantity)
    response = requests.post(f"{inventory_url}/inventory/used", json=ingredients)
    available = response.json().get("available", False)
    if available:
        return jsonify({"coffeeType": coffee_type, "quantity": quantity, "status": "Confirmed"})
    else:
        return jsonify({"coffeeType": coffee_type, "quantity": quantity, "status": "Out of Stock"})