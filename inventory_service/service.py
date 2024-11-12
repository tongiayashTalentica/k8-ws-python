import os
from flask import jsonify, request

# Read environment variables at the start and store them in memory
ESPRESSO_SHOT_QUANTITY = int(os.getenv('ESPRESSO_SHOT_QUANTITY', 0))
MILK_QUANTITY = int(os.getenv('MILK_QUANTITY', 0))
HOT_WATER_QUANTITY = int(os.getenv('HOT_WATER_QUANTITY', 0))
MILK_FOAM_QUANTITY = int(os.getenv('MILK_FOAM_QUANTITY', 0))

# Initialize the stock dictionary
current_stock = {
    "espressoShot": ESPRESSO_SHOT_QUANTITY,
    "milk": MILK_QUANTITY,
    "hotWater": HOT_WATER_QUANTITY,
    "milkFoam": MILK_FOAM_QUANTITY
}

def get_stock():
    stock = {
        "espressoShot": {"name": "Espresso Shot", "quantity": current_stock["espressoShot"]},
        "milk": {"name": "Milk", "quantity": current_stock["milk"]},
        "hotWater": {"name": "Hot Water", "quantity": current_stock["hotWater"]},
        "milkFoam": {"name": "Milk Foam", "quantity": current_stock["milkFoam"]}
    }
    return jsonify(stock)

def use_ingredient():
    ingredients = request.json
    available = True

    # Check if all requested quantities are available
    for ingredient, quantity in ingredients.items():
        if ingredient in current_stock and current_stock[ingredient] < quantity:
            available = False
            break

    # Update the stock if all requested quantities are available
    if available:
        for ingredient, quantity in ingredients.items():
            if ingredient in current_stock:
                current_stock[ingredient] -= quantity

    return jsonify({"available": available})