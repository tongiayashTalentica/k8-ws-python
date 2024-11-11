from flask import Flask
from multiprocessing import Process
from inventory_service.routes import inventory_bp
from order_service.routes import order_bp

def create_inventory_app():
    app = Flask(__name__)
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    return app

def create_order_app():
    app = Flask(__name__)
    app.register_blueprint(order_bp, url_prefix='/order')
    return app

def run_inventory_app():
    app = create_inventory_app()
    app.run(port=8082)

def run_order_app():
    app = create_order_app()
    app.run(port=8083)

if __name__ == '__main__':
    inventory_process = Process(target=run_inventory_app)
    order_process = Process(target=run_order_app)
    inventory_process.start()
    order_process.start()
    inventory_process.join()
    order_process.join()