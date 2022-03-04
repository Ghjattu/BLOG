import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'aw$OgdklqL')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOG_ARTICLE_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
