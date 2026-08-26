from flask import Blueprint, request, jsonify
from models import db, Activity

activity_bp = Blueprint('activity', __name__)


@activity_bp.route('', methods=['GET'])
def get_activities():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    keyword = request.args.get('keyword')
    is_featured = request.args.get('is_featured')

    query = Activity.query
    if category:
        query = query.filter(Activity.category == category)
    if keyword:
        query = query.filter(Activity.title.contains(keyword))
    if is_featured is not None:
        query = query.filter(Activity.is_featured == (is_featured == 'true'))

    pagination = query.order_by(Activity.publish_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@activity_bp.route('/<int:id>', methods=['GET'])
def get_activity(id):
    activity = Activity.query.get_or_404(id)
    activity.views += 1
    db.session.commit()
    return jsonify({'code': 200, 'data': activity.to_dict()})


@activity_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = ['文化节', '校园活动', '国际交流', '社区康养', '公益支教',
                  '学术研讨', '文创大赛']
    return jsonify({'code': 200, 'data': categories})


@activity_bp.route('', methods=['POST'])
def create_activity():
    data = request.get_json()
    activity = Activity(
        title=data['title'], category=data['category'],
        publish_date=data.get('publish_date'),
        publisher=data.get('publisher'),
        views=data.get('views', 0),
        summary=data.get('summary'), content=data.get('content'),
        tags=','.join(data.get('tags', [])),
        cover_image=data.get('cover_image'),
        is_featured=data.get('is_featured', False)
    )
    db.session.add(activity)
    db.session.commit()
    return jsonify({'code': 201, 'data': activity.to_dict(), 'message': '创建成功'})


@activity_bp.route('/<int:id>', methods=['PUT'])
def update_activity(id):
    activity = Activity.query.get_or_404(id)
    data = request.get_json()
    for field in ['title', 'category', 'publish_date', 'publisher', 'summary',
                  'content', 'cover_image', 'is_featured']:
        if field in data:
            setattr(activity, field, data[field])
    if 'tags' in data:
        activity.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': activity.to_dict(), 'message': '更新成功'})


@activity_bp.route('/<int:id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get_or_404(id)
    db.session.delete(activity)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})
