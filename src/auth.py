from flask import Blueprint, request,jsonify, make_response, abort, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from src.database import db, User
from src.constants.http_status_code import HTTP_400_BAD_REQUEST, HTTP_201_CREATED,  HTTP_409_CONFLICT
import validators


auth=Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth.route('/register', methods=['POST'])
def register():
    try:
        username=request.json.get('username')
        email=request.json.get('email')
        password=request.json.get('password')
        print(username,email,password)

      
        pwd_hash=generate_password_hash(password)
        user=User(username=username, email=email, password=pwd_hash)
        db.session.add(user)
        db.session.commit()
        return  {"User": "me"}, HTTP_201_CREATED
    except  Exception as e:
        print(e)

        
        return jsonify({"error": "Something went wrong"}), HTTP_400_BAD_REQUEST

    
@auth.route("/me", methods=["GET"])
def me ():
    return {"User": "me"}

