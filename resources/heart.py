from flask import Response, request
from database.models import Heart
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class HeartsApi(Resource):

    def get(self):
        hearts = Heart.objects().to_json()
        return Response(hearts, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        heart = Heart(**body).save()
        id = heart.id
        return {"id": str(id)}, 200

class HeartApi(Resource):

    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Heart.objects.get(id=id).update(**body)
        return "Heart was successfully updated", 200

    @jwt_required()
    def delete(self, id):
        Heart.objects.get(id=id).delete()
        return "Heart was successfully deleted", 200
