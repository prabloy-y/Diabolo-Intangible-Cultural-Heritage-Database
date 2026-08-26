from flask import Blueprint, request, jsonify
from models import db, TeamMember, Contributor

about_bp = Blueprint('about', __name__)


# ==================== 团队成员 ====================
@about_bp.route('/team', methods=['GET'])
def get_team():
    members = TeamMember.query.order_by(TeamMember.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [m.to_dict() for m in members]})


@about_bp.route('/team', methods=['POST'])
def create_member():
    data = request.get_json()
    member = TeamMember(
        name=data['name'], role=data['role'],
        title=data.get('title'), major=data.get('major'),
        description=data.get('description'),
        avatar=data.get('avatar'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(member)
    db.session.commit()
    return jsonify({'code': 201, 'data': member.to_dict(), 'message': '创建成功'})


@about_bp.route('/team/<int:id>', methods=['PUT'])
def update_member(id):
    member = TeamMember.query.get_or_404(id)
    data = request.get_json()
    for field in ['name', 'role', 'title', 'major', 'description', 'avatar',
                  'sort_order']:
        if field in data:
            setattr(member, field, data[field])
    db.session.commit()
    return jsonify({'code': 200, 'data': member.to_dict(), 'message': '更新成功'})


@about_bp.route('/team/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = TeamMember.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'code': 200, 'message': '删除成功'})


# ==================== 贡献者 ====================
@about_bp.route('/contributors', methods=['GET'])
def get_contributors():
    contributors = Contributor.query.order_by(Contributor.sort_order.asc()).all()
    return jsonify({'code': 200, 'data': [c.to_dict() for c in contributors]})


@about_bp.route('/contributors', methods=['POST'])
def create_contributor():
    data = request.get_json()
    contributor = Contributor(
        name=data['name'], contribution_type=data['contribution_type'],
        description=data.get('description'),
        sort_order=data.get('sort_order', 0)
    )
    db.session.add(contributor)
    db.session.commit()
    return jsonify({'code': 201, 'data': contributor.to_dict(), 'message': '创建成功'})
