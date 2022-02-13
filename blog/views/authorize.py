from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user, login_required

from blog.models import Admin
from blog.forms import LoginForm
from blog.utils import redirect_back

authorize_bp = Blueprint('authorize', __name__)


@authorize_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                return redirect_back()
    return render_template('authorize/login.html', form=form)


@authorize_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect_back()
