import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'douqu-zhufeng-secret-key-2025')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(BASE_DIR, 'kongzhu.db')
    )
    # 如需切换MySQL，取消下行注释并修改连接信息：
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/kongzhu_db?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'max_overflow': 20,
    }
    JSON_AS_ASCII = False
    JSONIFY_MIMETYPE = 'application/json; charset=utf-8'
