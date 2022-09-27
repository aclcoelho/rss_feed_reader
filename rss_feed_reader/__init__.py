from flask import Flask
from rss_feed_reader.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from rss_feed_reader.main.routes import main
    from rss_feed_reader.rss.routes import rss
    app.register_blueprint(main)
    app.register_blueprint(rss)
    
    return app