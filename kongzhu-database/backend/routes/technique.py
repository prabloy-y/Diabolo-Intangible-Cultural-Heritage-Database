from flask import Blueprint, request, jsonify
from models import db, Technique, FigureMove

technique_bp = Blueprint('technique', __name__)


# ==================== 核心技法 ====================
@technique_bp.route('/core', methods=['GET'])
def get_core_techniques():
    techniques = Technique.query.order_by(Technique.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [t.to_dict() for t in techniques]})


@technique_bp.route('/core', methods=['POST'])
def create_technique():
    data = request.get_json()
    technique = Technique(
        order_num=data['order_num'], name=data['name'],
        subtitle=data.get('subtitle'), description=data.get('description'),
        sub_techniques=','.join(data.get('sub_techniques', [])),
        category_tag=data.get('category_tag'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(technique)
    db.session.commit()
    return jsonify({'code': 201, 'data': technique.to_dict(), 'message': '创建成功'})


@technique_bp.route('/core/<int:id>', methods=['PUT'])
def update_technique(id):
    technique = Technique.query.get_or_404(id)
    data = request.get_json()
    for field in ['order_num', 'name', 'subtitle', 'description',
                  'category_tag', 'sort_order']:
        if field in data:
            setattr(technique, field, data[field])
    if 'sub_techniques' in data:
        technique.sub_techniques = ','.join(data['sub_techniques'])
    db.session.commit()
    return jsonify({'code': 200, 'data': technique.to_dict(), 'message': '更新成功'})


@technique_bp.route('/core/<int:id>', methods=['DELETE'])
def delete_technique(id):
    technique = Technique.query.get_or_404(id)
    db.session.delete(technique)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 花式动作 ====================
@technique_bp.route('/moves', methods=['GET'])
def get_moves():
    difficulty = request.args.get('difficulty', type=int)
    query = FigureMove.query
    if difficulty:
        query = query.filter(FigureMove.difficulty == difficulty)
    moves = query.order_by(FigureMove.order_num.asc()).all()
    return jsonify({'code': 200, 'data': [m.to_dict() for m in moves]})


@technique_bp.route('/moves', methods=['POST'])
def create_move():
    data = request.get_json()
    move = FigureMove(
        order_num=data['order_num'], name=data['name'],
        description=data.get('description'),
        difficulty=data.get('difficulty', 1),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(move)
    db.session.commit()
    return jsonify({'code': 201, 'data': move.to_dict(), 'message': '创建成功'})
