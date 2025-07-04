from .extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """
    User model for the application, inheriting from UserMixin for Flask-Login integration.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    modules = db.relationship('Module', backref='user', lazy=True) # Assuming a Module model exists 


class Module(db.Model):
    """ Module model representing a course or subject in the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    subject_code = db.Column(db.String(20), unique=True, nullable=False)
    target_grade = db.Column(db.Integer, nullable=False)  # How much the student aims to achieve
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assessments = db.relationship('Assessment', backref='module', lazy=True)  # Assuming an Assessment model exists


class Assessment(db.Model):
    """ Assessment model representing assessments/tests/tuts(interchangeble for now) within a module.
    """

    id = db.Column(db.Integer, primary_key=True)
    assessment_name = db.Column(db.String(150), nullable=False)
    assessment_weight = db.Column(db.Float, nullable=False)  # Weight of the assessment in the
    assessment_grade = db.Column(db.Float, nullable=False)  # Grade achieved in the assessment
    type = db.Column(db.String(50), nullable=False)  # Type of assessment (e.g., test, assignment)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)





    

    def __repr__(self):
        return f'<User {self.username}>'