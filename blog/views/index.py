from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)


# @index_bp.app_errorhandler(404)
# def page_not_found(e):
#     pass


@index_bp.route('/')
def index():
    return render_template('index/index.html')
