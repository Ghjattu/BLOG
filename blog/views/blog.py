from flask import Blueprint, render_template, request, current_app
from blog.models import Article, Tag, Category
from blog.utils import load_image

blog_bp = Blueprint('blog', __name__)

# images = ['https://tva2.sinaimg.cn/large/87c01ec7gy1fsnqqwn4vvj21kw0w04fx.jpg',
#           'https://tva4.sinaimg.cn/large/87c01ec7gy1fsnqqw43fkj21kw0w0h2l.jpg',
#           'https://tva4.sinaimg.cn/large/87c01ec7gy1fsnqqvhfrmj21kw0w0ne1.jpg',
#           'https://tva3.sinaimg.cn/large/87c01ec7gy1fsnqqw4ii2j21kw0w0dwy.jpg',
#           'https://tva2.sinaimg.cn/large/87c01ec7gy1fsnqqmq4fpj21kw0w07j3.jpg',
#           'https://tva1.sinaimg.cn/large/87c01ec7gy1fsnqqanu0wj21kw0w07h2.jpg',
#           'https://tva2.sinaimg.cn/large/87c01ec7gy1fsnqqmq4fpj21kw0w07j3.jpg',
#           'https://tva4.sinaimg.cn/large/87c01ec7gy1fsnqqf3p43j21kw0w0dtg.jpg',
#           'https://tva4.sinaimg.cn/large/87c01ec7gy1fsnqqmq4fpj21kw0w07j3.jpg',
#           'https://tva3.sinaimg.cn/large/87c01ec7gy1fsnqqw2vlij21kw0w0k8g.jpg']


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # 从查询字符串获取当前页数
    per_page = current_app.config['BLOG_ARTICLE_PER_PAGE']  # 每页文章数量
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(page, per_page=per_page, error_out=True)
    articles = pagination.items
    images = load_image(len(articles))
    return render_template('blog/index.html', articles=articles, images=images, pagination=pagination)


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


@blog_bp.route('/categories/<int:category_id>')
def show_category_articles(category_id):
    category = Category.query.get_or_404(category_id)
    articles = Article.query.with_parent(category).order_by(Article.timestamp.desc()).all()
    return render_template('blog/articles.html', articles=articles, category=category, is_category=True)


@blog_bp.route('/tags/<int:tag_id>')
def show_tag_articles(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    articles = Article.query.with_parent(tag).order_by(Article.timestamp.desc()).all()
    return render_template('blog/articles.html', articles=articles, tag=tag, is_category=False)


@blog_bp.route('/load_more')
def load_more():
    page = request.args.get('page', 1, type=int)  # 从查询字符串获取当前页数
    per_page = current_app.config['BLOG_ARTICLE_PER_PAGE']  # 每页文章数量
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(page, per_page=per_page, error_out=True)
    articles = pagination.items
    images = load_image(len(articles))
    return render_template('_article.html', articles=articles, images=images, pagination=pagination)
