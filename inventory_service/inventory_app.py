from flask import Flask
from routes import inventory_bp

def create_inventory_app():
    app = Flask(__name__)
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    return app

def run_inventory_app():
    app = create_inventory_app()
    app.run(host='0.0.0.0', port=8082)

if __name__ == '__main__':
    run_inventory_app()