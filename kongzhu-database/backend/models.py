from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ==================== 政策文献 ====================
class Policy(db.Model):
    __tablename__ = 'policies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    level = db.Column(db.String(20), nullable=False, comment='国家级/地方级/省级')
    region = db.Column(db.String(50), nullable=True, comment='发布地区')
    publish_date = db.Column(db.Date, nullable=True)
    summary = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    cover_image = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(20), default='政策法规', comment='政策法规/学术研究')
    author = db.Column(db.String(100), nullable=True)
    pub_year = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'title': self.title, 'level': self.level,
            'region': self.region, 'publish_date': str(self.publish_date) if self.publish_date else None,
            'summary': self.summary, 'content': self.content,
            'tags': self.tags.split(',') if self.tags else [],
            'cover_image': self.cover_image, 'category': self.category,
            'author': self.author, 'pub_year': self.pub_year,
            'created_at': str(self.created_at)
        }


# ==================== 传承人物 ====================
class Inheritor(db.Model):
    __tablename__ = 'inheritors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False, comment='国家级/省级/市级')
    region = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=True, comment='头衔')
    avatar = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=True)
    teaching_years = db.Column(db.String(20), nullable=True)
    student_count = db.Column(db.String(20), nullable=True)
    achievements = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'level': self.level,
            'region': self.region, 'title': self.title, 'avatar': self.avatar,
            'description': self.description, 'teaching_years': self.teaching_years,
            'student_count': self.student_count,
            'achievements': self.achievements.split(',') if self.achievements else [],
            'tags': self.tags.split(',') if self.tags else [],
            'is_featured': self.is_featured, 'created_at': str(self.created_at)
        }


# ==================== 传承组织/机构 ====================
class HeritageOrg(db.Model):
    __tablename__ = 'heritage_orgs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    founded_year = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'founded_year': self.founded_year,
            'description': self.description,
            'tags': self.tags.split(',') if self.tags else [],
            'created_at': str(self.created_at)
        }


# ==================== 传承人层级统计 ====================
class InheritorStat(db.Model):
    __tablename__ = 'inheritor_stats'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(20), nullable=False)
    count = db.Column(db.Integer, default=0)
    provinces = db.Column(db.String(50), nullable=True)
    avg_years = db.Column(db.String(10), nullable=True)
    total_students = db.Column(db.String(20), nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'level': self.level, 'count': self.count,
            'provinces': self.provinces, 'avg_years': self.avg_years,
            'total_students': self.total_students
        }


# ==================== 活动新闻 ====================
class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False, comment='文化节/校园活动/国际交流/社区康养/公益支教')
    publish_date = db.Column(db.Date, nullable=True)
    publisher = db.Column(db.String(100), nullable=True)
    views = db.Column(db.Integer, default=0)
    summary = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    cover_image = db.Column(db.String(500), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'title': self.title, 'category': self.category,
            'publish_date': str(self.publish_date) if self.publish_date else None,
            'publisher': self.publisher, 'views': self.views,
            'summary': self.summary, 'content': self.content,
            'tags': self.tags.split(',') if self.tags else [],
            'cover_image': self.cover_image, 'is_featured': self.is_featured,
            'created_at': str(self.created_at)
        }


# ==================== 学习课程 ====================
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(20), nullable=False, comment='入门课程/中级课程/高级课程/专项课程')
    age_group = db.Column(db.String(50), nullable=True, comment='少儿/青少年/成人/中老年')
    instructor = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Float, default=0)
    review_count = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), default=0)
    episode_count = db.Column(db.Integer, default=0)
    thumbnail = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    duration = db.Column(db.String(20), nullable=True)
    student_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'title': self.title, 'category': self.category,
            'age_group': self.age_group, 'instructor': self.instructor,
            'rating': float(self.rating), 'review_count': self.review_count,
            'description': self.description, 'price': float(self.price),
            'episode_count': self.episode_count, 'thumbnail': self.thumbnail,
            'tags': self.tags.split(',') if self.tags else [],
            'duration': self.duration, 'student_count': self.student_count,
            'created_at': str(self.created_at)
        }


# ==================== 扬竹康养十式 ====================
class KangyangStyle(db.Model):
    __tablename__ = 'kangyang_styles'

    id = db.Column(db.Integer, autoincrement=True)
    order_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'order': self.order_num,
            'name': self.name, 'description': self.description
        }


# ==================== 竞赛信息 ====================
class Competition(db.Model):
    __tablename__ = 'competitions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    level = db.Column(db.String(20), nullable=False, comment='国内赛事/国际赛事/地方赛事/省级赛事')
    event_date = db.Column(db.Date, nullable=True)
    location = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    categories = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'title': self.title, 'level': self.level,
            'event_date': str(self.event_date) if self.event_date else None,
            'location': self.location, 'description': self.description,
            'categories': self.categories.split(',') if self.categories else [],
            'tags': self.tags.split(',') if self.tags else [],
            'created_at': str(self.created_at)
        }


# ==================== 竞赛获奖记录 ====================
class Award(db.Model):
    __tablename__ = 'awards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    competition_name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    winner = db.Column(db.String(100), nullable=False)
    award_type = db.Column(db.String(20), nullable=False, comment='金奖/银奖/铜奖')
    year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'competition_name': self.competition_name,
            'category': self.category, 'winner': self.winner,
            'award_type': self.award_type, 'year': self.year
        }


# ==================== 文创产品 ====================
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False, comment='传统工艺/国潮文创/教学图书/智能空竹/数字产品')
    price = db.Column(db.Numeric(10, 2), default=0)
    original_price = db.Column(db.Numeric(10, 2), default=0)
    rating = db.Column(db.Float, default=0)
    review_count = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(500), nullable=True)
    is_hot = db.Column(db.Boolean, default=False)
    is_new = db.Column(db.Boolean, default=False)
    is_tech = db.Column(db.Boolean, default=False)
    is_gift = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'category': self.category,
            'price': float(self.price), 'original_price': float(self.original_price),
            'rating': float(self.rating), 'review_count': self.review_count,
            'description': self.description,
            'tags': self.tags.split(',') if self.tags else [],
            'image': self.image, 'is_hot': self.is_hot, 'is_new': self.is_new,
            'is_tech': self.is_tech, 'is_gift': self.is_gift,
            'created_at': str(self.created_at)
        }


# ==================== 历史大事年表 ====================
class HistoryEvent(db.Model):
    __tablename__ = 'history_events'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dynasty = db.Column(db.String(50), nullable=False)
    period = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'dynasty': self.dynasty, 'period': self.period,
            'title': self.title, 'description': self.description,
            'sort_order': self.sort_order
        }


# ==================== 空竹名称演变 ====================
class NameEvolution(db.Model):
    __tablename__ = 'name_evolutions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dynasty = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(200), nullable=True)
    meaning = db.Column(db.Text, nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'dynasty': self.dynasty, 'name': self.name,
            'source': self.source, 'meaning': self.meaning,
            'sort_order': self.sort_order
        }


# ==================== 地域流派 ====================
class RegionalSchool(db.Model):
    __tablename__ = 'regional_schools'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'subtitle': self.subtitle,
            'description': self.description,
            'tags': self.tags.split(',') if self.tags else [],
            'sort_order': self.sort_order
        }


# ==================== 核心技法 ====================
class Technique(db.Model):
    __tablename__ = 'techniques'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    subtitle = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    sub_techniques = db.Column(db.String(500), nullable=True)
    category_tag = db.Column(db.String(20), nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'order_num': self.order_num,
            'name': self.name, 'subtitle': self.subtitle,
            'description': self.description,
            'sub_techniques': self.sub_techniques.split(',') if self.sub_techniques else [],
            'category_tag': self.category_tag, 'sort_order': self.sort_order
        }


# ==================== 花式动作 ====================
class FigureMove(db.Model):
    __tablename__ = 'figure_moves'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.Integer, default=1)
    tags = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'order_num': self.order_num,
            'name': self.name, 'description': self.description,
            'difficulty': self.difficulty,
            'tags': self.tags.split(',') if self.tags else []
        }


# ==================== 影像资料 ====================
class GalleryItem(db.Model):
    __tablename__ = 'gallery_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False, comment='纪录片/教学视频/活动纪实/历史照片/VR全景')
    duration = db.Column(db.String(20), nullable=True)
    views = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=True)
    thumbnail = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id, 'title': self.title, 'category': self.category,
            'duration': self.duration, 'views': self.views,
            'description': self.description, 'thumbnail': self.thumbnail,
            'tags': self.tags.split(',') if self.tags else [],
            'created_at': str(self.created_at)
        }


# ==================== 国际交流-国家 ====================
class IntlCountry(db.Model):
    __tablename__ = 'intl_countries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'description': self.description,
            'tags': self.tags.split(',') if self.tags else [],
            'sort_order': self.sort_order
        }


# ==================== 国际组织 ====================
class IntlOrg(db.Model):
    __tablename__ = 'intl_orgs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    founded_year = db.Column(db.String(20), nullable=True)
    headquarters = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    tags = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'founded_year': self.founded_year,
            'headquarters': self.headquarters, 'description': self.description,
            'tags': self.tags.split(',') if self.tags else []
        }


# ==================== 国际交流大事记 ====================
class IntlTimeline(db.Model):
    __tablename__ = 'intl_timeline'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'year': self.year, 'title': self.title,
            'description': self.description, 'sort_order': self.sort_order
        }


# ==================== 关于我们-团队成员 ====================
class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=True)
    major = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    avatar = db.Column(db.String(500), nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'role': self.role,
            'title': self.title, 'major': self.major,
            'description': self.description, 'avatar': self.avatar,
            'sort_order': self.sort_order
        }


# ==================== 贡献者 ====================
class Contributor(db.Model):
    __tablename__ = 'contributors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    contribution_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sort_order = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name,
            'contribution_type': self.contribution_type,
            'description': self.description, 'sort_order': self.sort_order
        }


# ==================== 数据统计概览 ====================
class DashboardStat(db.Model):
    __tablename__ = 'dashboard_stats'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stat_key = db.Column(db.String(50), unique=True, nullable=False)
    stat_value = db.Column(db.String(50), nullable=False)
    stat_label = db.Column(db.String(100), nullable=False)
    sub_label = db.Column(db.String(200), nullable=True)
    icon = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(20), nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'stat_key': self.stat_key,
            'stat_value': self.stat_value, 'stat_label': self.stat_label,
            'sub_label': self.sub_label, 'icon': self.icon, 'color': self.color
        }


# ==================== 学习路径阶段 ====================
class LearningStage(db.Model):
    __tablename__ = 'learning_stages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage_order = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            'id': self.id, 'stage_order': self.stage_order,
            'name': self.name, 'description': self.description,
            'duration': self.duration
        }
