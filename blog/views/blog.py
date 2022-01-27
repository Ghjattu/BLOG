from flask import Blueprint, render_template, request, current_app
from blog.models import Post

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # 从查询字符串获取当前页数
    per_page = current_app.config['BLOG_POST_PER_PAGE']  # 每页文章数量
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page, error_out=True)
    posts = pagination.items
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/show_post.html', post=post)
