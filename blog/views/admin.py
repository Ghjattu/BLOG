from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from blog.models import Article, Category, Tag
from blog.extensions import db, cache
from blog.utils import redirect_back, load_image
from blog.forms import ArticleForm

admin_bp = Blueprint('admin', __name__)


@admin_bp.before_request
@login_required
def login_protect():
    pass


@admin_bp.route('/dashboard')
def manage():
    articles = Article.query.order_by(Article.timestamp.desc()).all()
    categories = Category.query.all()
    tags = Tag.query.all()
    return render_template('admin/dashboard.html', articles=articles, categories=categories, tags=tags)


@admin_bp.route('/delete/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    cache.delete('view/%s' % url_for('blog.index'))  # 删除缓存
    return redirect_back()


@admin_bp.route('/dashboard/new/article', methods=['GET', 'POST'])
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = Category.query.get(form.category.data)
        tags = [Tag.query.get(tag_id) for tag_id in form.tag.data]
        image = load_image(1)[0]
        article = Article(title=title, body=body, category=category, tags=tags, image=image)
        db.session.add(article)
        db.session.commit()
        cache.delete('view/%s' % url_for('blog.index'))  # 删除缓存
        return redirect(url_for('blog.show_article', article_id=article.id))
    return render_template('admin/new_article.html', form=form)
