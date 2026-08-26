from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db
from routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    register_routes(app)

    with app.app_context():
        db.create_all()

    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({'code': 200, 'message': '中国空竹数据库API运行正常', 'status': 'ok'})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'code': 404, 'message': '请求的资源不存在'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({'code': 500, 'message': '服务器内部错误'}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
