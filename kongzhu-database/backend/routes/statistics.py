from flask import Blueprint, jsonify
from models import db, DashboardStat
from sqlalchemy import text

statistics_bp = Blueprint('statistics', __name__)


@statistics_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    stats = DashboardStat.query.order_by(DashboardStat.id.asc()).all()
    return jsonify({'code': 200, 'data': [s.to_dict() for s in stats]})


@statistics_bp.route('/totals', methods=['GET'])
def get_totals():
    counts = {}
    for name, model_name in [
        ('inheritors', 'Inheritor'), ('policies', 'Policy'),
        ('courses', 'Course'), ('activities', 'Activity'),
        ('gallery_items', 'GalleryItem'), ('products', 'Product'),
        ('intl_countries', 'IntlCountry'), ('figure_moves', 'FigureMove')
    ]:
        counts[name] = db.session.execute(
            text(f"SELECT COUNT(*) FROM {model_name.lower()}s")
        ).scalar()
    return jsonify({'code': 200, 'data': counts})


@statistics_bp.route('/growth', methods=['GET'])
def get_growth():
    data = {
        'labels': ['2023Q1', '2023Q2', '2023Q3', '2023Q4', '2024Q1',
                   '2024Q2', '2024Q3', '2024Q4', '2025Q1', '2025Q2'],
        'datasets': [
            {'label': '传承人档案(人)', 'data': [8, 15, 22, 25, 27, 29, 30, 31, 32, 32],
             'borderColor': '#C53030', 'backgroundColor': 'rgba(197,48,48,0.1)'},
            {'label': '政策文献(条)', 'data': [20, 45, 68, 85, 105, 120, 138, 148, 152, 156],
             'borderColor': '#D69E2E', 'backgroundColor': 'rgba(214,158,46,0.1)'},
            {'label': '教学课程(集)', 'data': [5, 12, 18, 25, 30, 35, 40, 45, 47, 48],
             'borderColor': '#1A365D', 'backgroundColor': 'rgba(26,54,93,0.1)'},
            {'label': '活动新闻(篇)', 'data': [15, 38, 65, 95, 140, 175, 210, 235, 252, 260],
             'borderColor': '#38A169', 'backgroundColor': 'rgba(56,161,105,0.1)'}
        ]
    }
    return jsonify({'code': 200, 'data': data})
