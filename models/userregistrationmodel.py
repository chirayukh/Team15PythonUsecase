import flask_sqlalchemy
from datetime import date
import json

db=flask_sqlalchemy.SQLAlchemy()


class UserRegistrationModel(db.Model):
    __tablename__="userdetails"
    __table__args__={'schema':'bms_schema'}

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False )
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)
    dob = db.Column(db.String(50), nullable=False )
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    pan = db.Column(db.String(100), unique=True, nullable=False)
    contactno = db.Column(db.String(100), unique=True, nullable=False)

    #def _init_(self,id, name,username,password,dob,email,address,state,country,pan,contactno):
     #   self.id=

    def __repr__(self):
         return json.dumps({"id":self.id,"name":self.name,"username":self.username,"password":self.password,"dob":self.dob,"email":self.email,"address":self.address,"state":self.state,"country":self.country,"pan": self.pan,"contactno":self.contactno},indent=4)


    

