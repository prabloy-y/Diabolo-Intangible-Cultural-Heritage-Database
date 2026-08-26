from flask import Blueprint, request, jsonify
from models import db, IntlCountry, IntlOrg, IntlTimeline

international_bp = Blueprint('international', __name__)


# ==================== 国家传播 ====================
@international_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = IntlCountry.query.order_by(IntlCountry.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [c.to_dict() for c in countries]})


@international_bp.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    country = IntlCountry(
        name=data['name'], description=data.get('description'),
        tags=','.join(data.get('tags', [])),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(country)
    db.session.commit()
    return jsonify({'code': 201, 'data': country.to_dict(), 'message': '创建成功'})


@international_bp.route('/countries/<int:id>', methods=['PUT'])
def update_country(id):
    country = IntlCountry.query.get_or_404(id)
    data = request.get_json()
    for field in ['name', 'description', 'sort_order']:
        if field in data:
            setattr(country, field, data[field])
    if 'tags' in data:
        country.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': country.to_dict(), 'message': '更新成功'})


@international_bp.route('/countries/<int:id>', methods=['DELETE'])
def delete_country(id):
    country = IntlCountry.query.get_or_404(id)
    db.session.delete(country)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 国际组织 ====================
@international_bp.route('/orgs', methods=['GET'])
def get_orgs():
    orgs = IntlOrg.query.all()
    return jsonify({'code': 200, 'data': [o.to_dict() for o in orgs]})


@international_bp.route('/orgs', methods=['POST'])
def create_org():
    data = request.get_json()
    org = IntlOrg(
        name=data['name'], founded_year=data.get('founded_year'),
        headquarters=data.get('headquarters'),
        description=data.get('description'),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(org)
    db.session.commit()
    return jsonify({'code': 201, 'data': org.to_dict(), 'message': '创建成功'})


# ==================== 国际交流大事记 ====================
@international_bp.route('/timeline', methods=['GET'])
def get_timeline():
    timeline = IntlTimeline.query.order_by(IntlTimeline.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [t.to_dict() for t in timeline]})


@international_bp.route('/timeline', methods=['POST'])
def create_timeline():
    data = request.get_json()
    timeline = IntlTimeline(
        year=data['year'], title=data['title'],
        description=data.get('description'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(timeline)
    db.session.commit()
    return jsonify({'code': 201, 'data': timeline.to_dict(), 'message': '创建成功'})
