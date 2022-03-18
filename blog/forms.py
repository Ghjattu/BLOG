from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, SelectMultipleField, \
    TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length

from blog.models import Category, Tag


class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6, 128)])
    remember = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class ArticleForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired(), Length(1, 60)])
    category = SelectField(u'分类', coerce=int, default=1)
    tag = SelectMultipleField(u'标签', coerce=int)
    body = TextAreaField(u'正文', validators=[DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]
        self.tag.choices = [(tag.id, tag.name)
                            for tag in Tag.query.order_by(Tag.name).all()]


class CategoryForm(FlaskForm):
    name = StringField(u'分类名', validators=[DataRequired(), Length(1, 20)])
    new_category_submit = SubmitField()

    @staticmethod
    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError(u'存在同名分类')


class TagForm(FlaskForm):
    name = StringField(u'标签名', validators=[DataRequired(), Length(1, 20)])
    new_tag_submit = SubmitField()

    @staticmethod
    def validate_name(self, field):
        if Tag.query.filter_by(name=field.data).first():
            raise ValidationError(u'存在同名标签')
