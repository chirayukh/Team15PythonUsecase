from flask import Flask,request,jsonify
from flask_smorest import Api
from resources.userregistration import blpUserReg,db
import flask_sqlalchemy

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['API_TITLE']='Bank Management REST API'
app.config['API_VERSION']='v1'
app.config['OPENAPI_VERSION']='3.0.3'
app.config['OPENAPI_URL_PREFIX']='/'
app.config['OPENAPI_SWAGGER_UI_PATH']='/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL']='https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost:5432/bms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db.init_app(app)

api=Api(app)
api.register_blueprint(blpUserReg)


