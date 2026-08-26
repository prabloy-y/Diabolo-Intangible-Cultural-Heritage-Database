"""
种子数据脚本 - 基于前端HTML内容填充MySQL数据
使用前请先确保数据库已创建（运行init_db.sql），并修改config.py中的数据库连接信息。
运行：python seed_data.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from datetime import date
from app import create_app
from models import db, Policy, Inheritor, HeritageOrg, InheritorStat
from models import Activity, Course, KangyangStyle, LearningStage
from models import Competition, Award, Product
from models import HistoryEvent, NameEvolution, RegionalSchool
from models import Technique, FigureMove, GalleryItem
from models import IntlCountry, IntlOrg, IntlTimeline
from models import TeamMember, Contributor, DashboardStat


def seed_all():
    app = create_app()
    with app.app_context():
        print("开始填充种子数据...")

        # ==================== 政策文献 ====================
        policies = [
            Policy(title='《中华人民共和国非物质文化遗产法》', level='国家级', region='全国',
                   publish_date=date(2011, 6, 1),
                   summary='我国非物质文化遗产保护的纲领性法律文件，确立了非遗保护的指导思想、基本原则和法律制度。',
                   tags='非遗法,法律保护,传承人制度', category='政策法规', pub_year='2011'),
            Policy(title='抖空竹入选第一批国家级非物质文化遗产名录', level='国家级', region='全国',
                   publish_date=date(2006, 5, 20),
                   summary='2006年5月20日，抖空竹经中华人民共和国国务院批准列入第一批国家级非物质文化遗产名录（编号：VI-4）。',
                   tags='国家级非遗名录,VI-4,首批入选', category='政策法规', pub_year='2006'),
            Policy(title='《关于进一步加强非物质文化遗产保护工作的意见》', level='国家级', region='全国',
                   publish_date=date(2021, 8, 1),
                   summary='2021年中共中央办公厅、国务院办公厅印发，提出到2025年非遗代表性项目得到有效保护。',
                   tags='保护意见,2025目标,2035远景', category='政策法规', pub_year='2021'),
            Policy(title='《国家级非物质文化遗产代表性传承人认定与管理办法》', level='国家级', region='全国',
                   publish_date=date(2019, 12, 1),
                   summary='规范国家级非遗代表性传承人的认定条件、程序、权利与义务，建立传承人年度评估和退出机制。',
                   tags='传承人认定,管理办法,评估机制', category='政策法规', pub_year='2019'),
            Policy(title='《中国传统工艺振兴计划》', level='国家级', region='全国',
                   publish_date=date(2017, 3, 1),
                   summary='国务院办公厅转发，提出要挖掘传统工艺的文化内涵，推动传统工艺品的生产性保护和产业化发展。',
                   tags='传统工艺,振兴计划,产业化', category='政策法规', pub_year='2017'),
            Policy(title='北京市非物质文化遗产保护条例', level='地方级', region='北京',
                   publish_date=date(2019, 6, 1),
                   summary='北京市将抖空竹列为重点保护项目，设立市级非遗保护专项资金，支持空竹文化进校园、进社区。',
                   tags='北京,非遗条例,专项资金', category='政策法规', pub_year='2019'),
            Policy(title='山东省非物质文化遗产条例', level='地方级', region='山东',
                   publish_date=date(2015, 12, 1),
                   summary='山东省将抖空竹纳入省级非遗保护体系，鼓励高校和科研机构开展空竹技艺研究和教学实践。',
                   tags='山东,非遗条例,高校合作', category='政策法规', pub_year='2015'),
            Policy(title='《抖空竹技艺的文化生态学研究》', level='国家级', region='全国',
                   publish_date=date(2024, 1, 1),
                   summary='从文化生态学视角出发，系统分析抖空竹技艺在当代社会的生存环境、传承困境与保护策略。',
                   tags='文化生态,传承困境,保护策略', category='学术研究', author='陈文华教授', pub_year='2024'),
            Policy(title='《数字人文视角下空竹非遗数字化保护研究》', level='国家级', region='全国',
                   publish_date=date(2023, 1, 1),
                   summary='探讨运用三维建模、动作捕捉和虚拟现实技术对抖空竹技艺进行数字化记录与再现的方法。',
                   tags='数字人文,数字化保护,三维建模', category='学术研究', author='林慧敏博士', pub_year='2023'),
            Policy(title='《空竹非遗在高校美育中的价值与路径》', level='国家级', region='全国',
                   publish_date=date(2024, 1, 1),
                   summary='分析抖空竹作为非遗项目在高校美育课程中的应用价值，提出"非遗+美育"融合教学模式。',
                   tags='高校美育,融合教学,青年传承', category='学术研究', author='王建国副教授', pub_year='2024'),
        ]
        db.session.add_all(policies)

        # ==================== 传承人物 ====================
        inheritors = [
            Inheritor(name='张国良', level='国家级', region='北京',
                      title='国家级抖空竹代表性传承人',
                      description='从事空竹技艺研究与教学40余年，熟练掌握六大核心技法及上百种花式动作，多次在国际空竹比赛中获得金奖。',
                      teaching_years='40年', student_count='300+',
                      achievements='国际金奖,40年教龄,弟子300+',
                      tags='国家级,北京,40年教龄,国际金奖', is_featured=True),
            Inheritor(name='李连元', level='国家级', region='北京',
                      title='国家级抖空竹代表性传承人',
                      description='出身空竹世家，全面掌握抖空竹传统技法和创新表演形式。在全国建立空竹传习站50余个，累计培训学员超过5000人次。',
                      teaching_years='35年', student_count='5000+',
                      achievements='传习站50+,学员5000+,国际传播',
                      tags='国家级,北京,传习站,国际传播', is_featured=True),
            Inheritor(name='孙光辉', level='省级', region='河南',
                      title='省级抖空竹代表性传承人',
                      description='独创"空竹舞"表演风格，将传统技艺与现代舞蹈、音乐艺术相结合。培养省级空竹运动员20余名。',
                      teaching_years='20年', student_count='500+',
                      achievements='空竹舞创始人,省级一等奖',
                      tags='省级,河南,空竹舞,创新表演'),
            Inheritor(name='张凤兰', level='省级', region='天津',
                      title='省级抖空竹代表性传承人',
                      description='专注女性空竹健身领域研究，开发适合中老年女性的空竹健身操课程体系，服务社区居民超3000人。',
                      teaching_years='18年', student_count='3000+',
                      achievements='空竹康养,社区3000+',
                      tags='省级,天津,空竹康养,社区推广'),
            Inheritor(name='刘振华', level='省级', region='山东',
                      title='省级抖空竹代表性传承人',
                      description='擅长双轮空竹和大型空竹表演技艺，创造"双龙戏珠""众星捧月"等团体表演套路。在山东省20余所中小学开展空竹特色课程。',
                      teaching_years='15年', student_count='2000+',
                      achievements='团体表演,校园20+',
                      tags='省级,山东,团体表演,校园推广'),
        ]
        db.session.add_all(inheritors)

        # ==================== 传承组织 ====================
        orgs = [
            HeritageOrg(name='北京市空竹运动协会', founded_year='2005',
                        description='北京市规模最大的空竹文化推广组织，注册会员超过2000人。',
                        tags='会员2000+,社区站点60+,年活动30+场'),
            HeritageOrg(name='烟台南山学院抖趣竹风团队', founded_year='2023',
                        description='由市级抖空竹代表性传承人杨文哲担任负责人的大学生创新创业团队。',
                        tags='青年传承,数字化保护,产学研联动'),
            HeritageOrg(name='中国空竹文化国际交流中心', founded_year='2010',
                        description='致力于推动空竹文化的国际传播与交流。已累计组织或参加50余场国际文化交流活动。',
                        tags='覆盖20+国家,国际活动50+'),
            HeritageOrg(name='中国非遗保护中心空竹研究室', founded_year='2015',
                        description='中国艺术研究院下属专业研究机构，已出版空竹研究专著6部，发表学术论文40余篇。',
                        tags='专著6部,论文40+'),
        ]
        db.session.add_all(orgs)

        # ==================== 传承人层级统计 ====================
        stats = [
            InheritorStat(level='国家级传承人', count=5, provinces='3省/市',
                          avg_years='35年', total_students='8,000+'),
            InheritorStat(level='省级传承人', count=12, provinces='8省/市',
                          avg_years='22年', total_students='15,000+'),
            InheritorStat(level='市级传承人', count=15, provinces='10省/市',
                          avg_years='15年', total_students='12,000+'),
        ]
        db.session.add_all(stats)

        # ==================== 活动新闻 ====================
        activities = [
            Activity(title='2025国际空竹文化节圆满落幕', category='文化节',
                     publish_date=date(2025, 6, 15), publisher='中国非遗保护中心',
                     views=3582,
                     summary='来自12个国家和地区的200余名空竹艺术家和爱好者齐聚一堂。',
                     tags='空竹文化节,国际交流,非遗活动,传承创新',
                     is_featured=True),
            Activity(title='"非遗进校园"空竹文化传承计划在全国百所中小学启动', category='校园活动',
                     publish_date=date(2025, 5, 20), publisher='教育部/文化和旅游部',
                     views=4891,
                     summary='首批在全国100所中小学开展空竹特色体育课程，预计覆盖学生超过5万人。',
                     tags='校园教育,百校计划,课程研发',
                     is_featured=True),
            Activity(title='空竹进校园，传统文化润童心', category='校园活动',
                     publish_date=date(2025, 6, 5), views=1245,
                     summary='空竹非遗传承人走进我市多所中小学开展空竹文化进校园活动。',
                     tags='校园,文化传承,互动教学'),
            Activity(title='"云上空竹"线上展示活动圆满结束', category='文化节',
                     publish_date=date(2025, 5, 28), views=2876,
                     summary='共收到来自全国各地的短视频投稿作品800余件，网络投票参与人数超过10万人。',
                     tags='线上活动,短视频,数字化传播'),
            Activity(title='"空竹康养进万家"社区公益行动正式启动', category='社区康养',
                     publish_date=date(2025, 5, 10), views=1892,
                     summary='覆盖全国50个社区的公益行动正式启动，培训100名空竹康养指导员。',
                     tags='社区康养,公益活动,扬竹康养'),
            Activity(title='"抖趣竹风"团队赴贵州山区开展空竹公益支教', category='公益支教',
                     publish_date=date(2025, 4, 25), views=2134,
                     summary='前往贵州省黔东南苗族侗族自治州山区小学开展为期两周的空竹公益支教活动。',
                     tags='公益支教,山区,留守儿童'),
            Activity(title='全国空竹技艺传承与创新研讨会在京召开', category='学术研讨',
                     publish_date=date(2025, 4, 15),
                     summary='发布了《空竹非遗传承发展北京共识》。',
                     tags='学术研讨,技术创新,北京共识'),
            Activity(title='中日韩空竹艺术交流活动在首尔举行', category='国际交流',
                     publish_date=date(2025, 3, 28),
                     summary='三国空竹艺术家同台献艺，签署了东亚空竹文化交流合作备忘录。',
                     tags='国际交流,东亚合作'),
            Activity(title='空竹非遗文创产品设计大赛作品征集启动', category='文创大赛',
                     publish_date=date(2025, 3, 10),
                     summary='面向全国高校和设计机构征集传统工艺创新、国潮文创设计等类别作品。',
                     tags='文创大赛,设计征集'),
        ]
        db.session.add_all(activities)

        # ==================== 课程 ====================
        courses = [
            Course(title='空竹零基础入门教程', category='入门课程',
                   instructor='张明教练', rating=4.9, review_count=128,
                   description='适合完全零基础的初学者，从空竹的基本结构、握法、启动方法开始教学。',
                   price=0, episode_count=12, tags='免费,新手入门,基础教学',
                   duration='每课15-20分钟', student_count=1280),
            Course(title='空竹中级技巧提升', category='中级课程',
                   instructor='李华教练', rating=4.8, review_count=96,
                   description='教授更复杂的空竹技巧，包括高抛、缠绕、跳跃、过桥、背穿等动作。',
                   price=99, episode_count=18, tags='中级,技巧提升,花式动作',
                   duration='每课20-25分钟', student_count=860),
            Course(title='空竹高级表演编排', category='高级课程',
                   instructor='王芳教练', rating=4.9, review_count=72,
                   description='教授高难度空竹技巧和表演编排，帮助学员打造专业级空竹表演节目。',
                   price=199, episode_count=24, tags='高级,表演编排,专业化',
                   duration='每课25-30分钟', student_count=520),
            Course(title='少儿启蒙课程', category='专项课程', age_group='少儿',
                   description='以趣味游戏化方式引导儿童认识空竹，培养手眼协调能力和专注力。12课时。',
                   price=0, episode_count=12, tags='趣味教学,12课时', student_count=350),
            Course(title='青少年系统课程', category='专项课程', age_group='青少年',
                   description='系统学习空竹技法，从入门到高级循序渐进，融入体育中考体能训练内容。48课时。',
                   price=299, episode_count=48, tags='系统教学,48课时', student_count=680),
            Course(title='成人技能课程', category='专项课程', age_group='成人',
                   description='针对成人学习特点设计的空竹技能培训课程，提供一对一陪练教学服务。灵活排课。',
                   price=399, episode_count=36, tags='灵活排课,一对一陪练', student_count=420),
            Course(title='中老年康养课程', category='专项课程', age_group='中老年',
                   description='自主研发"扬竹康养十式"专项课程，以低强度空竹运动结合中医养生理念。',
                   price=199, episode_count=10, tags='康养特色,中医融合', student_count=280),
        ]
        db.session.add_all(courses)

        # ==================== 扬竹康养十式 ====================
        kangyang = [
            KangyangStyle(order_num=1, name='竹起云台', description='激活肩部肌肉群，改善肩周血液循环，缓解肩颈僵硬'),
            KangyangStyle(order_num=2, name='竹舞清风', description='锻炼腕关节灵活性，增强上肢协调性，预防腕管综合征'),
            KangyangStyle(order_num=3, name='竹转乾坤', description='强化腰腹核心力量，改善腰椎活动度，预防腰肌劳损'),
            KangyangStyle(order_num=4, name='竹行龙步', description='提升下肢力量与平衡感，锻炼膝关节稳定性，预防跌倒'),
            KangyangStyle(order_num=5, name='竹韵养生', description='配合呼吸吐纳，调节心肺功能，缓解压力，改善睡眠质量'),
            KangyangStyle(order_num=6, name='竹影飞花', description='训练手眼协调与空间感知能力，延缓认知功能衰退'),
            KangyangStyle(order_num=7, name='竹海听涛', description='静态平衡训练，增强本体感觉，改善体态与脊柱健康'),
            KangyangStyle(order_num=8, name='竹映彩虹', description='双人配合动作，促进社交互动，预防老年孤独与抑郁'),
            KangyangStyle(order_num=9, name='竹梦悠扬', description='综合协调训练，整合全身肌群协同运动，提升身体综合素质'),
            KangyangStyle(order_num=10, name='竹道归真', description='放松收式训练，配合冥想与拉伸，完成整套康养运动的整理恢复'),
        ]
        db.session.add_all(kangyang)

        # ==================== 学习路径 ====================
        stages = [
            LearningStage(stage_order=1, name='启蒙阶段',
                          description='了解空竹结构，学习正确握竿姿势和启动方法，掌握基本抖法。',
                          duration='2-4周'),
            LearningStage(stage_order=2, name='基础阶段',
                          description='掌握捞、盘两大技法，学会5-8个基础花式动作。',
                          duration='1-3个月'),
            LearningStage(stage_order=3, name='进阶阶段',
                          description='全面掌握六大技法，熟练运用绕身、抛接等高级技术。',
                          duration='3-12个月'),
            LearningStage(stage_order=4, name='竞技/表演阶段',
                          description='创编个人风格化的表演套路，具备参加各级空竹比赛的能力。',
                          duration='1年以上'),
        ]
        db.session.add_all(stages)

        # ==================== 竞赛信息 ====================
        competitions = [
            Competition(title='2025年全国空竹锦标赛', level='国内赛事',
                        event_date=date(2025, 7, 18),
                        description='由国家体育总局社会体育指导中心主办的全国性空竹赛事。',
                        categories='个人赛,团体赛,创意编排', tags='国内赛事,全国锦标赛'),
            Competition(title='第十届亚洲空竹锦标赛', level='国际赛事',
                        event_date=date(2025, 9, 5),
                        description='亚洲地区规模最大的空竹赛事，来自12个国家和地区的选手将同台竞技。',
                        categories='传统技法,创新表演,青少年组', tags='国际赛事,亚洲锦标赛'),
            Competition(title='北京市第15届空竹艺术节', level='地方赛事',
                        event_date=date(2025, 8, 22),
                        description='北京市规模最大的空竹文化盛会。',
                        categories='市民组,学生组,大师表演', tags='地方赛事,艺术节'),
            Competition(title='山东省空竹技艺交流大赛', level='省级赛事',
                        event_date=date(2025, 10, 10),
                        description='山东省文化和旅游厅主办的省级空竹赛事。',
                        categories='传统技法,创新表演', tags='省级赛事,山东'),
        ]
        db.session.add_all(competitions)

        # ==================== 获奖记录 ====================
        awards = [
            Award(competition_name='全国空竹锦标赛', category='成人专业组·个人技巧',
                  winner='张国良', award_type='金奖', year=2024),
            Award(competition_name='亚洲空竹锦标赛', category='青少年组·个人技巧',
                  winner='陈晓明', award_type='金奖', year=2024),
            Award(competition_name='全国空竹锦标赛', category='成人业余组·团体表演',
                  winner='北京市空竹运动协会代表队', award_type='银奖', year=2024),
            Award(competition_name='国际空竹文化节', category='创意编排赛',
                  winner='孙光辉', award_type='金奖', year=2023),
            Award(competition_name='山东省空竹技艺交流大赛', category='青少年组·个人技巧',
                  winner='烟台南山学院代表队', award_type='金奖', year=2023),
            Award(competition_name='亚洲空竹锦标赛', category='成人专业组·双人配合',
                  winner='李连元、张凤兰', award_type='银奖', year=2023),
            Award(competition_name='国际空竹文化节', category='老年组·康养展示',
                  winner='北京市空竹协会老年队', award_type='金奖', year=2022),
        ]
        db.session.add_all(awards)

        # ==================== 文创产品 ====================
        products = [
            Product(name='传统工艺空竹套装', category='传统工艺',
                    price=198, original_price=298, rating=4.9, review_count=156,
                    description='精选优质毛竹手工制作，经典的"响"字纹样。',
                    tags='手工制作,毛竹,初学者', is_hot=True),
            Product(name='空竹非遗微电影合集', category='数字产品',
                    price=88, rating=4.8, review_count=92,
                    description='收录12部空竹非遗主题微电影和高清纪录片。',
                    tags='微电影,纪录片,数字产品'),
            Product(name='空竹技艺传承系列图书', category='教学图书',
                    price=128, rating=4.7, review_count=68,
                    description='《抖空竹技法大全》等三册套装，全彩印刷。',
                    tags='图书,三册套装,二维码', is_new=True),
            Product(name='空竹文化主题T恤', category='国潮文创',
                    price=68, rating=4.6, review_count=112,
                    description='国潮风空竹主题印花T恤，纯棉面料。',
                    tags='T恤,国潮,纯棉'),
            Product(name='智能科技空竹', category='智能空竹',
                    price=399, rating=4.9, review_count=45,
                    description='内置陀螺仪传感器，可实时监测转速、角度和动作轨迹。',
                    tags='智能,传感器,蓝牙,APP', is_tech=True),
            Product(name='空竹国潮帆布袋', category='国潮文创',
                    price=48, rating=4.8, review_count=88,
                    description='原创插画设计帆布袋，采用"抖趣竹风"IP形象。',
                    tags='帆布袋,国潮,环保'),
            Product(name='空竹非遗文创礼盒', category='传统工艺',
                    price=258, rating=5.0, review_count=32,
                    description='精装礼盒含手工空竹一个、文化读本一册。',
                    tags='礼盒,送礼,收藏', is_gift=True),
            Product(name='儿童启蒙空竹教具套装', category='教学图书',
                    price=98, rating=4.9, review_count=210,
                    description='专为6-12岁儿童设计的轻量化安全空竹教具。',
                    tags='儿童,安全,环保材质'),
        ]
        db.session.add_all(products)

        # ==================== 历史大事年表 ====================
        history_events = [
            HistoryEvent(dynasty='三国', period='220-280年',
                         title='三国时期 · 空竹雏形出现',
                         description='空竹的原始雏形出现，与古代陀螺游戏和百戏表演有着密切关联。',
                         sort_order=1),
            HistoryEvent(dynasty='唐代', period='618-907年',
                         title='唐代 · 空竹传入宫廷',
                         description='空竹传入宫廷贵族生活圈，敦煌壁画中出现了类似抖空竹的图像描绘。',
                         sort_order=2),
            HistoryEvent(dynasty='宋代', period='960-1279年',
                         title='宋代 · 空竹融入市民生活',
                         description='抖空竹成为城市市民文化娱乐的重要组成部分。《东京梦华录》对空竹有明确记载。',
                         sort_order=3),
            HistoryEvent(dynasty='明代', period='1368-1644年',
                         title='明代 · 空竹发展鼎盛时期',
                         description='《帝京景物略》对空竹进行详细描述，六大核心技法体系基本成型。天桥空竹流派兴起。',
                         sort_order=4),
            HistoryEvent(dynasty='清代', period='1644-1912年',
                         title='清代 · 空竹文化达到高峰',
                         description='乾隆年间空竹被收录于《四库全书》。北京天桥一带空竹艺人云集。',
                         sort_order=5),
            HistoryEvent(dynasty='民国', period='1912-1949年',
                         title='民国时期 · 空竹回归民间',
                         description='空竹从宫廷贵族娱乐全面回归民间，成为庙会、集市和节庆活动中的必备技艺。',
                         sort_order=6),
            HistoryEvent(dynasty='新中国', period='1950s-1970s',
                         title='新中国成立初期 · 纳入群众体育',
                         description='空竹被纳入群众体育运动体系，各级体育部门组织空竹培训和比赛。',
                         sort_order=7),
            HistoryEvent(dynasty='2006年', period='里程碑',
                         title='2006年 · 入选国家级非遗名录',
                         description='抖空竹经国务院批准列入第一批国家级非物质文化遗产名录（编号VI-4）。',
                         sort_order=8),
            HistoryEvent(dynasty='2011年', period='非遗法',
                         title='2011年 · 非遗法施行',
                         description='《中华人民共和国非物质文化遗产法》正式施行，空竹非遗保护获得法律制度保障。',
                         sort_order=9),
            HistoryEvent(dynasty='2025年', period='数字化时代',
                         title='2025年 · 数字化时代新篇章',
                         description='空竹非遗保护进入数字化、智能化新阶段。烟台南山学院建成中国空竹非遗数据库。',
                         sort_order=10),
        ]
        db.session.add_all(history_events)

        # ==================== 名称演变 ====================
        names = [
            NameEvolution(dynasty='三国', name='空钟', source='曹植《空竹赋》',
                          meaning='"空钟"意为中空而能发出钟声的玩具', sort_order=1),
            NameEvolution(dynasty='唐宋', name='空竹、扯铃', source='敦煌壁画、《东京梦华录》',
                          meaning='"空竹"之名始于此时，"扯铃"强调操作绳扯之动作', sort_order=2),
            NameEvolution(dynasty='明代', name='空钟、抖空竹', source='《帝京景物略》',
                          meaning='"抖空竹"三字组合首次出现在官方文献中', sort_order=3),
            NameEvolution(dynasty='清代', name='响簧、闷葫芦', source='《燕京岁时记》',
                          meaning='以声音特征命名，"响簧"形容其振动声响', sort_order=4),
            NameEvolution(dynasty='民国至今', name='抖空竹', source='现代通用称谓',
                          meaning='经国家非遗名录正式确认的标准名称', sort_order=5),
        ]
        db.session.add_all(names)

        # ==================== 地域流派 ====================
        schools = [
            RegionalSchool(name='北京派 · 天桥空竹',
                           description='以北京天桥地区为核心传承地，技法严谨规范，讲究"稳、准、美"。',
                           tags='技法严谨,哨口响亮,传承站60+', sort_order=1),
            RegionalSchool(name='天津派 · 津门空竹',
                           description='天津空竹以"巧"著称，注重技巧的灵活多变和即兴发挥。',
                           tags='灵活多变,说唱空竹,10+分会', sort_order=2),
            RegionalSchool(name='河南派 · 中原空竹',
                           description='中原空竹以"刚"见长，动作幅度大、力度强、气势磅礴。',
                           tags='刚劲有力,团体表演,起源地之一', sort_order=3),
            RegionalSchool(name='山东派 · 齐鲁空竹',
                           description='山东空竹以"实"为特色，将空竹与体育教育、康养健身紧密结合。',
                           tags='康养结合,产学研,扬竹康养十式', sort_order=4),
        ]
        db.session.add_all(schools)

        # ==================== 核心技法 ====================
        techniques = [
            Technique(order_num=1, name='抖', subtitle='基本抖法',
                      description='"抖"是空竹所有技法的基础和核心。通过双手协调上下拉动绳索，使空竹在绳索上保持高速平稳旋转。',
                      sub_techniques='正抖,反抖,基础技法', category_tag='基础技法', sort_order=1),
            Technique(order_num=2, name='捞', subtitle='捞取技法',
                      description='"捞"指用绳索从下方将空竹托起并接回的正常运转。',
                      sub_techniques='正捞,反捞,衔接技法', category_tag='衔接技法', sort_order=2),
            Technique(order_num=3, name='盘', subtitle='盘绳技法',
                      description='"盘"指将绳索缠绕在空竹轴心部位的技巧，是创造复杂花式动作的关键技法。',
                      sub_techniques='单盘,双盘,缠绕技巧', category_tag='缠绕技巧', sort_order=3),
            Technique(order_num=4, name='绕', subtitle='绕身技法',
                      description='"绕"指空竹围绕身体各部位进行圆周运动的技巧。',
                      sub_techniques='绕颈,绕腰,表演技法', category_tag='表演技法', sort_order=4),
            Technique(order_num=5, name='抛', subtitle='抛接技法',
                      description='"抛"是空竹技法中最具视觉冲击力的动作类别。',
                      sub_techniques='高抛,侧抛,高级技法', category_tag='高级技法', sort_order=5),
            Technique(order_num=6, name='接', subtitle='承接技法',
                      description='"接"是所有抛、捞动作的收尾环节。',
                      sub_techniques='绳接,杆接,收尾技法', category_tag='收尾技法', sort_order=6),
        ]
        db.session.add_all(techniques)

        # ==================== 花式动作 ====================
        moves = [
            FigureMove(order_num=1, name='金鸡上架',
                       description='将空竹从腿部下方穿过并向上抛起，在头顶上方用绳接住。',
                       difficulty=3, tags='腿部,高抛'),
            FigureMove(order_num=2, name='翻山越岭',
                       description='双臂交叉使空竹形成"8"字形运动轨迹，从身体一侧越过头顶到达另一侧。',
                       difficulty=2, tags='8字形,越头'),
            FigureMove(order_num=3, name='织女纺线',
                       description='模拟古代织女纺线的动作，将空竹在身前做快速的小圆周旋转。',
                       difficulty=3, tags='圆周旋转,柔美'),
            FigureMove(order_num=4, name='夜观银河',
                       description='将空竹以极高的速度垂直向上抛出3-5米。',
                       difficulty=4, tags='高抛,观赏性'),
            FigureMove(order_num=5, name='抬头望月',
                       description='身体后仰呈弓形，将空竹从身体后方抛过头部。',
                       difficulty=4, tags='后抛,弓形'),
            FigureMove(order_num=6, name='海底捞月',
                       description='弯腰下蹲，将空竹在贴近地面处进行捞取动作。',
                       difficulty=4, tags='下蹲,捞取'),
            FigureMove(order_num=7, name='双龙戏珠',
                       description='同时操控两个空竹（双手各一），使两个空竹在空中做对称或交替运动。',
                       difficulty=5, tags='双空竹,对称'),
            FigureMove(order_num=8, name='众星捧月',
                       description='多人（通常6-10人）围成圆圈同时抖空竹，配合音乐节奏进行统一的动作编排。',
                       difficulty=5, tags='团体,编排'),
        ]
        db.session.add_all(moves)

        # ==================== 影像资料 ====================
        gallery = [
            GalleryItem(title='《百年空竹——国家级非遗传承人口述史》',
                        category='纪录片', duration='45分钟', views=12580,
                        description='通过三位国家级传承人的口述，讲述近百年来空竹技艺的传承脉络。',
                        tags='口述史,国家级传承人'),
            GalleryItem(title='《空竹入门十二式——零基础完全教学》',
                        category='教学视频', duration='120分钟', views=28340,
                        description='由省级传承人亲自示范讲解，从握竿姿势到基本花式动作的全套教学视频。',
                        tags='零基础,多角度,慢动作'),
            GalleryItem(title='《2025国际空竹文化节开幕式精彩集锦》',
                        category='活动纪实', duration='30分钟', views=8920,
                        description='记录2025年国际空竹文化节开幕式的精彩瞬间。',
                        tags='文化节,开幕式,12国'),
        ]
        db.session.add_all(gallery)

        # ==================== 国际交流 ====================
        countries = [
            IntlCountry(name='日本', description='空竹经长崎传入日本。目前日本有超过50个空竹团体。',
                        tags='50+团体,年度赛事', sort_order=1),
            IntlCountry(name='韩国', description='韩国空竹协会自2002年成立以来发展迅速，会员超过3000人。',
                        tags='3000+会员,K-POP融合', sort_order=2),
            IntlCountry(name='法国', description='法国是欧洲空竹文化传播的中心。',
                        tags='欧洲中心,街头艺术', sort_order=3),
            IntlCountry(name='美国', description='美国空竹文化主要由华人社区推动发展。',
                        tags='IJA认证,校园推广', sort_order=4),
            IntlCountry(name='马来西亚', description='马来西亚是东南亚空竹文化最繁荣的国家之一。',
                        tags='华文学校,全国公开赛', sort_order=5),
            IntlCountry(name='新加坡', description='新加坡将空竹纳入国家体育理事会推广项目。',
                        tags='CCA课程,WDA创始国', sort_order=6),
        ]
        db.session.add_all(countries)

        intl_orgs = [
            IntlOrg(name='世界空竹联合会 (WDF)', founded_year='2015', headquarters='北京',
                    description='由18个国家和地区的空竹组织共同发起的国际性空竹组织。',
                    tags='18个成员国,世界锦标赛,规则制定'),
            IntlOrg(name='亚洲空竹联盟 (ADA)', founded_year='2008', headquarters='-',
                    description='由中日韩三国空竹协会联合发起，现有12个亚洲国家和地区会员。',
                    tags='12个成员国,亚洲锦标赛,教练认证'),
            IntlOrg(name='国际非遗空竹保护联盟 (ICH-DPA)', founded_year='2022', headquarters='-',
                    description='由中国非遗保护中心发起成立的国际学术性组织。',
                    tags='跨国共享,学术研究,传承人交流'),
        ]
        db.session.add_all(intl_orgs)

        timelines = [
            IntlTimeline(year='1985年', title='中国空竹首次亮相日本世博会',
                         description='中国空竹表演团在日本筑波世博会中国馆进行为期一周的表演。', sort_order=1),
            IntlTimeline(year='1998年', title='巴黎空竹俱乐部成立',
                         description='欧洲第一个专业空竹组织在巴黎成立。', sort_order=2),
            IntlTimeline(year='2008年', title='亚洲空竹联盟正式成立',
                         description='中日韩三国在北京签署协议，确立两年一届的亚洲锦标赛制度。', sort_order=3),
            IntlTimeline(year='2010年', title='上海世博会空竹文化周',
                         description='来自20多个国家的空竹艺术家进行了为期7天的联合展演。', sort_order=4),
            IntlTimeline(year='2015年', title='世界空竹联合会成立',
                         description='18个国家在北京共同发起成立WDF。', sort_order=5),
            IntlTimeline(year='2025年', title='中国空竹数据库国际版上线',
                         description='推出多语言国际版，支持中、英、日、韩、法五种语言。', sort_order=6),
        ]
        db.session.add_all(timelines)

        # ==================== 团队成员 ====================
        members = [
            TeamMember(name='杨文哲', role='项目负责人', title='市级抖空竹代表性传承人',
                       description='自幼习练空竹，师从国家级传承人，精通六大核心技法和50余种花式动作。',
                       sort_order=1),
            TeamMember(name='李明远', role='技术负责人', major='计算机科学与技术专业',
                       description='负责数据库系统架构设计、前端开发、VR/AI智能教学平台技术研发。',
                       sort_order=2),
            TeamMember(name='王晓雨', role='运营负责人', major='文化产业管理专业',
                       description='负责全媒体传播策略制定、文创产品设计开发、文旅研学项目运营。',
                       sort_order=3),
        ]
        db.session.add_all(members)

        # ==================== 贡献者 ====================
        contributors = [
            Contributor(name='杨文哲', contribution_type='技艺资料',
                        description='提供核心技法动作演示与课程体系设计', sort_order=1),
            Contributor(name='张国良', contribution_type='口述历史',
                        description='提供40年空竹传承经历的口述史资料', sort_order=2),
            Contributor(name='烟台南山学院', contribution_type='平台支持',
                        description='提供非遗工坊场地、数据库服务器和技术研发支持', sort_order=3),
            Contributor(name='李明远', contribution_type='系统开发',
                        description='数据库系统架构设计与前端开发', sort_order=4),
            Contributor(name='王晓雨', contribution_type='内容编辑',
                        description='政策文献整理、活动新闻采编与产品信息录入', sort_order=5),
            Contributor(name='中国非遗保护中心', contribution_type='学术支持',
                        description='提供空竹非遗保护政策文献与学术研究成果', sort_order=6),
        ]
        db.session.add_all(contributors)

        # ==================== 数据统计 ====================
        dashboard = [
            DashboardStat(stat_key='inheritors', stat_value='32', stat_label='收录传承人',
                          sub_label='国家级5人 · 省级12人 · 市级15人', color='primary'),
            DashboardStat(stat_key='policies', stat_value='156', stat_label='政策文献条目',
                          sub_label='国家级26 · 地方级98 · 学术32', color='secondary'),
            DashboardStat(stat_key='courses', stat_value='48', stat_label='教学课程',
                          sub_label='入门12 · 中级18 · 高级10 · 专项8', color='tertiary'),
            DashboardStat(stat_key='activities', stat_value='260+', stat_label='活动新闻记录',
                          sub_label='文化节 · 校园 · 国际 · 社区 · 公益', color='green'),
            DashboardStat(stat_key='gallery', stat_value='86', stat_label='影像视频资源',
                          sub_label='纪录片 · 教学片 · 活动纪实 · VR', color='purple'),
            DashboardStat(stat_key='products', stat_value='28', stat_label='文创产品',
                          sub_label='传统工艺 · 国潮 · 图书 · 智能', color='orange'),
            DashboardStat(stat_key='intl', stat_value='18', stat_label='国际覆盖国家',
                          sub_label='亚洲 · 欧洲 · 北美洲 · 大洋洲', color='blue'),
            DashboardStat(stat_key='moves', stat_value='200', stat_label='标准动作收录',
                          sub_label='六大技法 · 花式图谱 · 教学分解', color='red'),
        ]
        db.session.add_all(dashboard)

        db.session.commit()
        print("种子数据填充完成！共添加了以下数据：")
        print(f"  政策文献: {len(policies)} 条")
        print(f"  传承人物: {len(inheritors)} 人")
        print(f"  传承组织: {len(orgs)} 个")
        print(f"  活动新闻: {len(activities)} 条")
        print(f"  学习课程: {len(courses)} 门")
        print(f"  竞赛信息: {len(competitions)} 条")
        print(f"  获奖记录: {len(awards)} 条")
        print(f"  文创产品: {len(products)} 款")
        print(f"  历史事件: {len(history_events)} 条")
        print(f"  核心技法: {len(techniques)} 类")
        print(f"  花式动作: {len(moves)} 个")
        print(f"  影像资料: {len(gallery)} 条")
        print(f"  国际国家: {len(countries)} 个")
        print(f"  国际组织: {len(intl_orgs)} 个")


if __name__ == '__main__':
    seed_all()
