from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache
from flask_mail import Mail
from flask_talisman import Talisman

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'authorize.login'
csrf = CSRFProtect()
cache = Cache()
mail = Mail()
talisman = Talisman()


@login_manager.user_loader
def load_user(user_id):
    from blog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
