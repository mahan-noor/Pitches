from . import db
from flask_login import UserMixin
from . import login_manager




class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))





    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

# class Pitch(db.Model):
#     __tablename__ = 'pitch'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'pitches',lazy="dynamic")


#     def __repr__(self):
#         return f'User {self.name}'