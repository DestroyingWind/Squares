# from flask_mail import Mail
# from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from flask_redis import FlaskRedis


# mail = Mail()
# db = SQLAlchemy()
cache = Cache()
redis = FlaskRedis()