#-*- encoding=UTF-8 -*-

from nowstagram import app, db
from flask_script import Manager
from nowstagram.models import User, Image, Comment
import random

manager = Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0,1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User' + str(i+1), 'a' + str(i+1)))
        for j in range(0, 3):
            db.session.add(Image(get_image_url(), i+1))
            for k in range(0,3):
                db.session.add(Comment('this is a comment'+str(k), 3*i+1+j, i+1))

    db.session.commit()

    # print(1, User.query.all())
    # print(2, User.query.get(3))
    # print(3, User.query.filter_by(id=5).first())
    # print(4, User.query.order_by(User.id.desc()).offset(2).limit(2).all())
    # print(5, User.query.filter(User.username.endswith('0')).limit(3).all())
    # print(6, User.query.filter(and_(User.id > 88)).first_or_404()).all())
    # print(7, User.query.paginate(page=1, per_page=10).items)
    # user = User.query.get(1)
    # print(8, user.images)
    # image = Image.query.get(1)
    # print(9, image.user)

if __name__ == '__main__':
    manager.run()