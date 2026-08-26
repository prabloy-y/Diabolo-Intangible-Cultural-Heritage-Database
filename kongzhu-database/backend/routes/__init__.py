from .policy import policy_bp
from .heritage import heritage_bp
from .activity import activity_bp
from .course import course_bp
from .competition import competition_bp
from .product import product_bp
from .history import history_bp
from .technique import technique_bp
from .gallery import gallery_bp
from .international import international_bp
from .statistics import statistics_bp
from .about import about_bp


def register_routes(app):
    app.register_blueprint(policy_bp, url_prefix='/api/policies')
    app.register_blueprint(heritage_bp, url_prefix='/api/heritage')
    app.register_blueprint(activity_bp, url_prefix='/api/activities')
    app.register_blueprint(course_bp, url_prefix='/api/courses')
    app.register_blueprint(competition_bp, url_prefix='/api/competitions')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(history_bp, url_prefix='/api/history')
    app.register_blueprint(technique_bp, url_prefix='/api/techniques')
    app.register_blueprint(gallery_bp, url_prefix='/api/gallery')
    app.register_blueprint(international_bp, url_prefix='/api/international')
    app.register_blueprint(statistics_bp, url_prefix='/api/statistics')
    app.register_blueprint(about_bp, url_prefix='/api/about')
