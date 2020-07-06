from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api

from resources.assessment import AssessmentAPI
from resources.courses import CoursesAPI
from resources.questions import QuestionsAPI
from resources.reports import ReportsAPI
from resources.users import UsersAPI



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

api.add_resource(QuestionsAPI, '/api/questions/add', endpoint='questions_add', methods=["POST"])
api.add_resource(QuestionsAPI, '/api/questions/update', endpoint='questions_update', methods=["PATCH"])
api.add_resource(QuestionsAPI, '/api/questions/show', endpoint='questions_show', methods=["GET"])
api.add_resource(QuestionsAPI, '/api/questions/delete/<int:id>', endpoint='questions_delete', methods=["DELETE"])

api.add_resource(AssessmentAPI, '/api/assessment/add', endpoint='assessment_add', methods=["POST"])
api.add_resource(AssessmentAPI, '/api/assessment/update', endpoint='assessment_update', methods=["PATCH"])
api.add_resource(AssessmentAPI, '/api/assessment/show', endpoint='assessment_show', methods=["GET"])
api.add_resource(AssessmentAPI, '/api/assessment/delete/<int:id>', endpoint='assessment_delete', methods=["DELETE"])

api.add_resource(ReportsAPI, '/api/reports/add', endpoint='reports_add', methods=["POST"])
api.add_resource(ReportsAPI, '/api/reports/update', endpoint='reports_update', methods=["PATCH"])
api.add_resource(ReportsAPI, '/api/reports/show', endpoint='reports_show', methods=["GET"])
api.add_resource(ReportsAPI, '/api/reports/delete/<int:id>', endpoint='reports_delete', methods=["DELETE"])

api.add_resource(CoursesAPI, '/api/reports/add', endpoint='courses_add', methods=["POST"])
api.add_resource(CoursesAPI, '/api/reports/update', endpoint='courses_update', methods=["PATCH"])
api.add_resource(CoursesAPI, '/api/reports/show', endpoint='courses_show', methods=["GET"])
api.add_resource(CoursesAPI, '/api/reports/delete/<int:id>', endpoint='courses_delete', methods=["DELETE"])

api.add_resource(UsersAPI, '/api/users/add', endpoint='users_add', methods=["POST"])
api.add_resource(UsersAPI, '/api/users/update', endpoint='users_update', methods=["PATCH"])
api.add_resource(UsersAPI, '/api/users/show', endpoint='users_show', methods=["GET"])
api.add_resource(UsersAPI, '/api/users/delete/<int:id>', endpoint='users_delete', methods=["DELETE"])


@app.route('/')
def hello():
    return render_template("home.html")

@app.route("/authenticate")
def authenticate():
    return "authentication"

@app.route("/login")
def login():
    return "login"
    
@app.route("/logout")
def logout():
    return "logout"

if __name__ == '__main__':
    app.run(debug=True)