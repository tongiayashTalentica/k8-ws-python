from flask import Flask
from .routes import order_bp

def create_order_app():
    app = Flask(__name__)
    app.register_blueprint(order_bp, url_prefix='/order')
    return app

def run_order_app():
    app = create_order_app()
    app.run(port=8083)

if __name__ == '__main__':
    run_order_app()