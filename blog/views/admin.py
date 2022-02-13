from flask import Blueprint
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
@login_required
def login_protect():
    pass
