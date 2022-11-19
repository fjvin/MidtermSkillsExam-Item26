from .heart import HeartsApi, HeartApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(HeartsApi, "/api/hearts")
    api.add_resource(HeartApi, "/api/heart/<id>")
    api.add_resource(SignupApi, "/api/auth/signup")
    api.add_resource(LoginApi, "/api/auth/login")