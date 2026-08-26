from flask import Blueprint, request, jsonify
from models import db, Product

product_bp = Blueprint('product', __name__)


@product_bp.route('', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    keyword = request.args.get('keyword')

    query = Product.query
    if category:
        query = query.filter(Product.category == category)
    if keyword:
        query = query.filter(Product.name.contains(keyword))

    pagination = query.order_by(Product.id.asc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'code': 200, 'data': product.to_dict()})


@product_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = ['传统工艺', '国潮文创', '教学图书', '智能空竹', '数字产品']
    return jsonify({'code': 200, 'data': categories})


@product_bp.route('', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'], category=data['category'],
        price=data.get('price', 0),
        original_price=data.get('original_price', 0),
        rating=data.get('rating', 0),
        review_count=data.get('review_count', 0),
        description=data.get('description'),
        tags=','.join(data.get('tags', [])),
        image=data.get('image'),
        is_hot=data.get('is_hot', False),
        is_new=data.get('is_new', False),
        is_tech=data.get('is_tech', False),
        is_gift=data.get('is_gift', False)
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'code': 201, 'data': product.to_dict(), 'message': '创建成功'})


@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    for field in ['name', 'category', 'price', 'original_price', 'rating',
                  'review_count', 'description', 'image',
                  'is_hot', 'is_new', 'is_tech', 'is_gift']:
        if field in data:
            setattr(product, field, data[field])
    if 'tags' in data:
        product.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': product.to_dict(), 'message': '更新成功'})


@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})
