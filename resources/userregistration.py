from flask_smorest import Blueprint
from flask.views import MethodView
from flask import Flask,request,jsonify
from models.userregistrationmodel import UserRegistrationModel,db

blpUserReg=Blueprint("userReg",__name__,description="UserRegistrationBP")

@blpUserReg.route("/userRegistration")
class UserRegistration(MethodView):
    def post(self):
        request_data=request.get_json()
        print(request_data)
        new_user=UserRegistrationModel(**request_data)
        db.session.add(new_user)
        db.session.commit()
        return {"User": new_user.username},201

    def get(self):
           all_users=UserRegistrationModel.query.all() 
           return {"users":str(all_users)}



