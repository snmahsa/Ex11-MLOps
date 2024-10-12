from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=True, unique=True)
    password = db.Column(db.String(100), nullable=True, unique=True)

class TrackerInput(db.Model):   
    # __tablename__ = 'tracker_input' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mean_radius = db.Column(db.Float,nullable=False)
    mean_perimeter = db.Column(db.Float,nullable=False)
    mean_area = db.Column(db.Float,nullable=False)
    mean_concavity = db.Column(db.Float,nullable=False)
    mean_concave_points = db.Column(db.Float,nullable=False)
    worst_radius = db.Column(db.Float,nullable=False)
    worst_perimeter = db.Column(db.Float,nullable=False)
    worst_area = db.Column(db.Float,nullable=False)
    worst_concavity = db.Column(db.Float,nullable=False)
    worst_concave_points = db.Column(db.Float,nullable=False)
    result =db.Column(db.Integer,nullable=False)
