from flask import Blueprint, request, jsonify
from models import db, HistoryEvent, NameEvolution, RegionalSchool

history_bp = Blueprint('history', __name__)


# ==================== 历史大事年表 ====================
@history_bp.route('/events', methods=['GET'])
def get_events():
    events = HistoryEvent.query.order_by(HistoryEvent.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [e.to_dict() for e in events]})


@history_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = HistoryEvent(
        dynasty=data['dynasty'], period=data.get('period'),
        title=data['title'], description=data.get('description'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({'code': 201, 'data': event.to_dict(), 'message': '创建成功'})


@history_bp.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    event = HistoryEvent.query.get_or_404(id)
    data = request.get_json()
    for field in ['dynasty', 'period', 'title', 'description', 'sort_order']:
        if field in data:
            setattr(event, field, data[field])
    db.session.commit()
    return jsonify({'code': 200, 'data': event.to_dict(), 'message': '更新成功'})


@history_bp.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = HistoryEvent.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 名称演变 ====================
@history_bp.route('/names', methods=['GET'])
def get_names():
    names = NameEvolution.query.order_by(NameEvolution.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [n.to_dict() for n in names]})


# ==================== 地域流派 ====================
@history_bp.route('/schools', methods=['GET'])
def get_schools():
    schools = RegionalSchool.query.order_by(RegionalSchool.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [s.to_dict() for s in schools]})
