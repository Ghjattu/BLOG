import os
import re

import click
import markdown
from flask import Flask, Markup, redirect, url_for

from blog.extensions import db, moment, login_manager, csrf
from blog.models import Admin, Category
from blog.settings import config
from blog.views.admin import admin_bp
from blog.views.authorize import authorize_bp
from blog.views.blog import blog_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('blog')
    app.config.from_object(config[config_name])
    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_error_handlers(app)
    register_commands(app)
    register_template_context(app)
    register_template_filter(app)

    return app


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(authorize_bp, url_prefix='/authorize')
    app.register_blueprint(admin_bp, url_prefix='/admin')


def register_extensions(app):
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return redirect(url_for('blog.index'))

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('blog.index'))

    @app.errorhandler(405)
    def method_not_allowed(e):
        return redirect(url_for('blog.index'))

    @app.errorhandler(500)
    def internal_server_error(e):
        return redirect(url_for('blog.index'))


def register_commands(app):
    @app.cli.command()
    @click.option('--category', default=10)
    @click.option('--tag', default=5)
    @click.option('--article', default=50)
    def forge(category, tag, article):
        from blog.vdata import fake_admin, fake_articles, fake_categories, fake_tags

        db.drop_all()
        db.create_all()

        fake_admin()
        fake_categories(category)
        fake_tags(tag)
        fake_articles(article)

        click.echo('Done.')


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.all()
        return dict(admin=admin, categories=categories)


def register_template_filter(app):
    @app.template_filter('MDtoHTML')
    def md_to_html(mdcontent):
        content = Markup(markdown.markdown(mdcontent, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.fenced_code',
            'markdown.extensions.toc'
        ]))
        return content

    @app.template_filter('MDfilter')
    def md_filter(mdcontent):
        pattern = re.compile(r'[TOC\[\]#$]')
        return re.sub(pattern, '', mdcontent)
