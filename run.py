from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Lucerde1@@localhost:3306/testdb?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = False

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)