import random

from sqlalchemy.exc import IntegrityError

from blog.models import Admin, Post, Category, Tag
from blog.extensions import db
from faker import Faker

fake = Faker()


def fake_admin():
    admin = Admin(
        username='Ghjattu',
        blog_title='Ghjattu\'s blog',
        signature='I want to put a ding in the universe.'
    )
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(1000),
            timestamp=fake.date_time_this_year(),
            category=Category.query.get(random.randint(1, Category.query.count())),
            tags=[Tag.query.get(random.randint(1, Tag.query.count())) for _ in range(2)]
        )
        db.session.add(post)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_categories(count=10):
    category = Category(name='Default')
    db.session.add(category)
    db.session.commit()

    for i in range(count):
        category = Category(
            name=fake.word()
        )
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_tags(count=5):
    tag = Tag(name='Default')
    db.session.add(tag)
    db.session.commit()

    for i in range(count):
        tag = Tag(
            name=fake.word()
        )
        db.session.add(tag)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
