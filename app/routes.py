from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from app.models import db, User
from werkzeug.security import generate_password_hash
import jsonify
import app



bp = Blueprint('api', __name__)
api = Api(bp)

# Define the home route
@bp.route('/')
def home():
    return "Welcome to the Home Page!"

api = Blueprint('api', __name__)
api = Api(bp)

#@api.route('/data')
#def get_data():
    #return jsonify(data="Here is some data")

#app.register_blueprint(api, url_prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('email', type=str, required=True, help='Email is required')
parser.add_argument('mobile_no', type=int, required=True, help='Mobile number is required')
parser.add_argument('gender', type=str, required=True, help='Gender is required')

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'mobile_no': user.mobile_no,
            'gender': user.gender
        }

    def put(self, user_id):
        args = parser.parse_args()
        user = User.query.get_or_404(user_id)
        user.username = args['username']
        user.email = args['email']
        user.mobile_no = args['mobile_no']
        user.gender = args['gender']
        db.session.commit()
        return {'message': 'User updated successfully'},200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'},200

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'mobile_no': user.mobile_no,
            'gender': user.gender
        } for user in users]

    def post(self):
        print("posted")
        args = parser.parse_args()
        print("Received data:", args)  # Debugging line
        user = User(username=args['username'], email=args['email'], mobile_no=args['mobile_no'], gender=args['gender'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
