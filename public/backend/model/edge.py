import datetime
import enum

from config.db import db


class Status(enum.Enum):
    Y = 'Yes'
    N = 'No'


class Project(db.Model):
    __tablename__ = 'tbl_projects'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(Status), default='Y')
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class Assessment_question(db.model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Enum(Status), default='Y')
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    