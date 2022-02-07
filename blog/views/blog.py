from flask import Blueprint, render_template, request, current_app
from blog.models import Article, Tag

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # 从查询字符串获取当前页数
    per_page = current_app.config['BLOG_POST_PER_PAGE']  # 每页文章数量
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(page, per_page=per_page, error_out=True)
    articles = pagination.items
    return render_template('blog/index.html', articles=articles)


@blog_bp.route('/articles/<int:article_id>')
def show_article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('blog/article.html', article=article)


@blog_bp.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('blog/tags.html', tags=tags)


@blog_bp.route('/archive')
def show_archive():
    articles = Article.query.order_by(Article.timestamp.desc()).all()
    return render_template('blog/archive.html', articles=articles)
