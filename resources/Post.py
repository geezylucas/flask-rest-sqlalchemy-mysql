from flask import request
from flask_restful import Resource
from Models import db, Post, PostSchema

posts_schema = PostSchema(many=True)
post_schema = PostSchema()


class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        posts = posts_schema.dump(posts)
        return {'status': 'success', 'data': posts}, 200

    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_post)
        db.session.commit()
        result = post_schema.dump(new_post)
        return {"status": 'success', 'data': result}, 201


class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        post = post_schema.dump(post)
        return {'status': 'success', 'data': post}, 200

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        post = post_schema.dump(post)
        return {'status': 'success', 'data': post}, 200

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204
