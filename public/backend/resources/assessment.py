from flask import request
from flask_restful import Resource

from sqlalchemy import func

class AssessmentAPI(Resource):
    def get(self):
        return 'true'
    
    def post(self):
        return 'true'

    def delete(self):
        return 'true'

    def put(self):
        return 'true'