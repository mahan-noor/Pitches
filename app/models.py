from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitch',backref = 'role',lazy="dynamic")
    comment = db.relationship('Comment',backref = 'role',lazy="dynamic")
    upvote = db.relationship('Upvote',backref = 'role',lazy="dynamic")
    downvote = db.relationship('Downvote',backref = 'role',lazy="dynamic")
    password_hash = db.Column(db.String(255))





    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'




class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

        

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),index = True)
    post = db.Column(db.String(255))
    category = db.Column(db.String(255), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comment = db.relationship('Comment',backref = 'user',lazy="dynamic")
    upvote = db.relationship('Upvote',backref = 'user',lazy="dynamic")
    downvote = db.relationship('Downvote',backref = 'user',lazy="dynamic")


  
    


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


        
    def __repr__(self):
        return f'Pitch {self.post}'



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'



class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        comments = Upvote.query.filter_by(pitch_id=id).all()

        return downvotes


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'




class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        comments = Downvote.query.filter_by(pitch_id=pitch_id).all()

        return downvotes


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'



