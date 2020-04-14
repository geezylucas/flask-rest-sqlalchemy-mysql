from flask import Blueprint
from flask_restful import Api
from resources.Post import PostListResource, PostResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
