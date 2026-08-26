from flask import Blueprint, request, jsonify
from models import db, GalleryItem

gallery_bp = Blueprint('gallery', __name__)


@gallery_bp.route('/items', methods=['GET'])
def get_items():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    category = request.args.get('category')
    keyword = request.args.get('keyword')

    query = GalleryItem.query
    if category:
        query = query.filter(GalleryItem.category == category)
    if keyword:
        query = query.filter(GalleryItem.title.contains(keyword))

    pagination = query.order_by(GalleryItem.views.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@gallery_bp.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = GalleryItem.query.get_or_404(id)
    item.views += 1
    db.session.commit()
    return jsonify({'code': 200, 'data': item.to_dict()})


@gallery_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = ['纪录片', '教学视频', '活动纪实', '历史照片', 'VR全景']
    return jsonify({'code': 200, 'data': categories})


@gallery_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = GalleryItem(
        title=data['title'], category=data['category'],
        duration=data.get('duration'), views=data.get('views', 0),
        description=data.get('description'),
        thumbnail=data.get('thumbnail'),
        tags=','.join(data.get('tags', []))
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'code': 201, 'data': item.to_dict(), 'message': '创建成功'})


@gallery_bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = GalleryItem.query.get_or_404(id)
    data = request.get_json()
    for field in ['title', 'category', 'duration', 'description', 'thumbnail']:
        if field in data:
            setattr(item, field, data[field])
    if 'tags' in data:
        item.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': item.to_dict(), 'message': '更新成功'})


@gallery_bp.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = GalleryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})
