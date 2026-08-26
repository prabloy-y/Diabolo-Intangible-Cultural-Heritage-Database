from flask import Blueprint, request, jsonify
from models import db, Competition, Award

competition_bp = Blueprint('competition', __name__)


# ==================== 竞赛信息 ====================
@competition_bp.route('', methods=['GET'])
def get_competitions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    level = request.args.get('level')
    keyword = request.args.get('keyword')

    query = Competition.query
    if level:
        query = query.filter(Competition.level == level)
    if keyword:
        query = query.filter(Competition.title.contains(keyword))

    pagination = query.order_by(Competition.event_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@competition_bp.route('/<int:id>', methods=['GET'])
def get_competition(id):
    competition = Competition.query.get_or_404(id)
    return jsonify({'code': 200, 'data': competition.to_dict()})


@competition_bp.route('', methods=['POST'])
def create_competition():
    data = request.get_json()
    competition = Competition(
        title=data['title'], level=data['level'],
        event_date=data.get('event_date'),
        location=data.get('location'),
        description=data.get('description'),
        categories=','.join(data.get('categories', [])),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(competition)
    db.session.commit()
    return jsonify({'code': 201, 'data': competition.to_dict(), 'message': '创建成功'})


@competition_bp.route('/<int:id>', methods=['PUT'])
def update_competition(id):
    competition = Competition.query.get_or_404(id)
    data = request.get_json()
    for field in ['title', 'level', 'event_date', 'location', 'description']:
        if field in data:
            setattr(competition, field, data[field])
    if 'categories' in data:
        competition.categories = ','.join(data['categories'])
    if 'tags' in data:
        competition.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': competition.to_dict(), 'message': '更新成功'})


@competition_bp.route('/<int:id>', methods=['DELETE'])
def delete_competition(id):
    competition = Competition.query.get_or_404(id)
    db.session.delete(competition)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 获奖记录 ====================
@competition_bp.route('/awards', methods=['GET'])
def get_awards():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    year = request.args.get('year', type=int)
    award_type = request.args.get('award_type')

    query = Award.query
    if year:
        query = query.filter(Award.year == year)
    if award_type:
        query = query.filter(Award.award_type == award_type)

    pagination = query.order_by(Award.year.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@competition_bp.route('/awards', methods=['POST'])
def create_award():
    data = request.get_json()
    award = Award(
        competition_name=data['competition_name'],
        category=data.get('category'),
        winner=data['winner'],
        award_type=data['award_type'],
        year=data['year']
    )
    db.session.add(award)
    db.session.commit()
    return jsonify({'code': 201, 'data': award.to_dict(), 'message': '创建成功'})
