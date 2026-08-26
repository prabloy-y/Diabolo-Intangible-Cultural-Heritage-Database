from flask import Blueprint, request, jsonify
from models import db, Policy

policy_bp = Blueprint('policy', __name__)


@policy_bp.route('', methods=['GET'])
def get_policies():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    level = request.args.get('level')
    category = request.args.get('category')
    keyword = request.args.get('keyword')

    query = Policy.query
    if level:
        query = query.filter(Policy.level == level)
    if category:
        query = query.filter(Policy.category == category)
    if keyword:
        query = query.filter(Policy.title.contains(keyword))

    pagination = query.order_by(Policy.publish_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total,
        'page': page,
        'per_page': per_page
    })


@policy_bp.route('/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    return jsonify({'code': 200, 'data': policy.to_dict()})


@policy_bp.route('/levels', methods=['GET'])
def get_levels():
    levels = ['国家级', '地方级', '省级']
    return jsonify({'code': 200, 'data': levels})


@policy_bp.route('', methods=['POST'])
def create_policy():
    data = request.get_json()
    policy = Policy(
        title=data['title'], level=data.get('level', ''),
        region=data.get('region'), publish_date=data.get('publish_date'),
        summary=data.get('summary'), content=data.get('content'),
        tags=','.join(data.get('tags', [])),
        cover_image=data.get('cover_image'),
        category=data.get('category', '政策法规'),
        author=data.get('author'), pub_year=data.get('pub_year')
    )
    db.session.add(policy)
    db.session.commit()
    return jsonify({'code': 201, 'data': policy.to_dict(), 'message': '创建成功'})


@policy_bp.route('/<int:policy_id>', methods=['PUT'])
def update_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    data = request.get_json()
    for field in ['title', 'level', 'region', 'publish_date', 'summary',
                  'content', 'cover_image', 'category', 'author', 'pub_year']:
        if field in data:
            setattr(policy, field, data[field])
    if 'tags' in data:
        policy.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': policy.to_dict(), 'message': '更新成功'})


@policy_bp.route('/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    policy = Policy.query.get_or_404(policy_id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})
