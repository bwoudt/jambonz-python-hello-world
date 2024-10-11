from quart import Quart
from app.routes import routes
from app.config import Config

def create_app():
    app = Quart(__name__)
    
    # Load config
    app.config.from_object(Config)
    
    # Register routes
    app.register_blueprint(routes)
    
    return app
