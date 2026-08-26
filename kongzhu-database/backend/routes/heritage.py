from flask import Blueprint, request, jsonify
from models import db, Inheritor, HeritageOrg, InheritorStat

heritage_bp = Blueprint('heritage', __name__)


# ==================== 传承人物 ====================
@heritage_bp.route('/inheritors', methods=['GET'])
def get_inheritors():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    level = request.args.get('level')
    region = request.args.get('region')
    keyword = request.args.get('keyword')

    query = Inheritor.query
    if level:
        query = query.filter(Inheritor.level == level)
    if region:
        query = query.filter(Inheritor.region == region)
    if keyword:
        query = query.filter(Inheritor.name.contains(keyword))

    pagination = query.order_by(
        Inheritor.level.asc(), Inheritor.id.asc()
    ).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@heritage_bp.route('/inheritors/<int:id>', methods=['GET'])
def get_inheritor(id):
    inheritor = Inheritor.query.get_or_404(id)
    return jsonify({'code': 200, 'data': inheritor.to_dict()})


@heritage_bp.route('/inheritors', methods=['POST'])
def create_inheritor():
    data = request.get_json()
    inheritor = Inheritor(
        name=data['name'], level=data['level'], region=data['region'],
        title=data.get('title'), avatar=data.get('avatar'),
        description=data.get('description'),
        teaching_years=data.get('teaching_years'),
        student_count=data.get('student_count'),
        achievements=','.join(data.get('achievements', [])),
        tags=','.join(data.get('tags', [])),
        is_featured=data.get('is_featured', False)
    )
    db.session.add(inheritor)
    db.session.commit()
    return jsonify({'code': 201, 'data': inheritor.to_dict(), 'message': '创建成功'})


@heritage_bp.route('/inheritors/<int:id>', methods=['PUT'])
def update_inheritor(id):
    inheritor = Inheritor.query.get_or_404(id)
    data = request.get_json()
    for field in ['name', 'level', 'region', 'title', 'avatar', 'description',
                  'teaching_years', 'student_count', 'is_featured']:
        if field in data:
            setattr(inheritor, field, data[field])
    if 'achievements' in data:
        inheritor.achievements = ','.join(data['achievements'])
    if 'tags' in data:
        inheritor.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': inheritor.to_dict(), 'message': '更新成功'})


@heritage_bp.route('/inheritors/<int:id>', methods=['DELETE'])
def delete_inheritor(id):
    inheritor = Inheritor.query.get_or_404(id)
    db.session.delete(inheritor)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 传承组织 ====================
@heritage_bp.route('/orgs', methods=['GET'])
def get_orgs():
    orgs = HeritageOrg.query.order_by(HeritageOrg.id.asc()).all()
    return jsonify({'code': 200, 'data': [org.to_dict() for org in orgs]})


@heritage_bp.route('/orgs', methods=['POST'])
def create_org():
    data = request.get_json()
    org = HeritageOrg(
        name=data['name'], founded_year=data.get('founded_year'),
        description=data.get('description'),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(org)
    db.session.commit()
    return jsonify({'code': 201, 'data': org.to_dict(), 'message': '创建成功'})


# ==================== 层级统计 ====================
@heritage_bp.route('/stats', methods=['GET'])
def get_stats():
    stats = InheritorStat.query.order_by(InheritorStat.id.asc()).all()
    return jsonify({'code': 200, 'data': [s.to_dict() for s in stats]})
