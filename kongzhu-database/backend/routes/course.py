from flask import Blueprint, request, jsonify
from models import db, Course, KangyangStyle, LearningStage

course_bp = Blueprint('course', __name__)


# ==================== 课程 ====================
@course_bp.route('', methods=['GET'])
def get_courses():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    age_group = request.args.get('age_group')
    keyword = request.args.get('keyword')

    query = Course.query
    if category:
        query = query.filter(Course.category == category)
    if age_group:
        query = query.filter(Course.age_group == age_group)
    if keyword:
        query = query.filter(Course.title.contains(keyword))

    pagination = query.order_by(Course.id.asc()).paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify({
        'code': 200,
        'data': [item.to_dict() for item in pagination.items],
        'total': pagination.total, 'page': page, 'per_page': per_page
    })


@course_bp.route('/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify({'code': 200, 'data': course.to_dict()})


@course_bp.route('', methods=['POST'])
def create_course():
    data = request.get_json()
    course = Course(
        title=data['title'], category=data['category'],
        age_group=data.get('age_group'),
        instructor=data.get('instructor'),
        rating=data.get('rating', 0),
        review_count=data.get('review_count', 0),
        description=data.get('description'),
        price=data.get('price', 0),
        episode_count=data.get('episode_count', 0),
        thumbnail=data.get('thumbnail'),
        tags=','.join(data.get('tags', [])),
        duration=data.get('duration'),
        student_count=data.get('student_count', 0)
    )
    db.session.add(course)
    db.session.commit()
    return jsonify({'code': 201, 'data': course.to_dict(), 'message': '创建成功'})


@course_bp.route('/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()
    for field in ['title', 'category', 'age_group', 'instructor', 'rating',
                  'review_count', 'description', 'price', 'episode_count',
                  'thumbnail', 'duration', 'student_count']:
        if field in data:
            setattr(course, field, data[field])
    if 'tags' in data:
        course.tags = ','.join(data['tags'])
    db.session.commit()
    return jsonify({'code': 200, 'data': course.to_dict(), 'message': '更新成功'})


@course_bp.route('/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 扬竹康养十式 ====================
@course_bp.route('/kangyang', methods=['GET'])
def get_kangyang():
    styles = KangyangStyle.query.order_by(KangyangStyle.order_num.asc()).all()
    return jsonify({'code': 200, 'data': [s.to_dict() for s in styles]})


# ==================== 学习路径 ====================
@course_bp.route('/stages', methods=['GET'])
def get_stages():
    stages = LearningStage.query.order_by(LearningStage.stage_order.asc()).all()
    return jsonify({'code': 200, 'data': [s.to_dict() for s in stages]})
