-- 中国空竹数据库系统
-- MySQL Schema
-- 创建数据库
CREATE DATABASE IF NOT EXISTS kongzhu_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE kongzhu_db;

-- ==================== 政策文献 ====================
CREATE TABLE IF NOT EXISTS policies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    level VARCHAR(20) NOT NULL COMMENT '国家级/地方级/省级',
    region VARCHAR(50) COMMENT '发布地区',
    publish_date DATE,
    summary TEXT,
    content TEXT,
    tags VARCHAR(500),
    cover_image VARCHAR(500),
    category VARCHAR(20) DEFAULT '政策法规' COMMENT '政策法规/学术研究',
    author VARCHAR(100),
    pub_year VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 传承人物 ====================
CREATE TABLE IF NOT EXISTS inheritors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    level VARCHAR(20) NOT NULL COMMENT '国家级/省级/市级',
    region VARCHAR(50) NOT NULL,
    title VARCHAR(100) COMMENT '头衔',
    avatar VARCHAR(500),
    description TEXT,
    teaching_years VARCHAR(20),
    student_count VARCHAR(20),
    achievements VARCHAR(500),
    tags VARCHAR(500),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 传承组织 ====================
CREATE TABLE IF NOT EXISTS heritage_orgs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    founded_year VARCHAR(20),
    description TEXT,
    tags VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 传承人层级统计 ====================
CREATE TABLE IF NOT EXISTS inheritor_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    level VARCHAR(20) NOT NULL,
    count INT DEFAULT 0,
    provinces VARCHAR(50),
    avg_years VARCHAR(10),
    total_students VARCHAR(20)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 活动新闻 ====================
CREATE TABLE IF NOT EXISTS activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL COMMENT '文化节/校园活动/国际交流/社区康养/公益支教',
    publish_date DATE,
    publisher VARCHAR(100),
    views INT DEFAULT 0,
    summary TEXT,
    content TEXT,
    tags VARCHAR(500),
    cover_image VARCHAR(500),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 学习课程 ====================
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    category VARCHAR(20) NOT NULL COMMENT '入门课程/中级课程/高级课程/专项课程',
    age_group VARCHAR(50) COMMENT '少儿/青少年/成人/中老年',
    instructor VARCHAR(50),
    rating FLOAT DEFAULT 0,
    review_count INT DEFAULT 0,
    description TEXT,
    price DECIMAL(10,2) DEFAULT 0,
    episode_count INT DEFAULT 0,
    thumbnail VARCHAR(500),
    tags VARCHAR(500),
    duration VARCHAR(20),
    student_count INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 扬竹康养十式 ====================
CREATE TABLE IF NOT EXISTS kangyang_styles (
    id INT AUTO_INCREMENT,
    order_num INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 竞赛信息 ====================
CREATE TABLE IF NOT EXISTS competitions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    level VARCHAR(20) NOT NULL COMMENT '国内赛事/国际赛事/地方赛事/省级赛事',
    event_date DATE,
    location VARCHAR(200),
    description TEXT,
    categories VARCHAR(500),
    tags VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 竞赛获奖记录 ====================
CREATE TABLE IF NOT EXISTS awards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    competition_name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    winner VARCHAR(100) NOT NULL,
    award_type VARCHAR(20) NOT NULL COMMENT '金奖/银奖/铜奖',
    year INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 文创产品 ====================
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL COMMENT '传统工艺/国潮文创/教学图书/智能空竹/数字产品',
    price DECIMAL(10,2) DEFAULT 0,
    original_price DECIMAL(10,2) DEFAULT 0,
    rating FLOAT DEFAULT 0,
    review_count INT DEFAULT 0,
    description TEXT,
    tags VARCHAR(500),
    image VARCHAR(500),
    is_hot BOOLEAN DEFAULT FALSE,
    is_new BOOLEAN DEFAULT FALSE,
    is_tech BOOLEAN DEFAULT FALSE,
    is_gift BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 历史大事年表 ====================
CREATE TABLE IF NOT EXISTS history_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dynasty VARCHAR(50) NOT NULL,
    period VARCHAR(100),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    sort_order INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 空竹名称演变 ====================
CREATE TABLE IF NOT EXISTS name_evolutions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dynasty VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    source VARCHAR(200),
    meaning TEXT,
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 地域流派 ====================
CREATE TABLE IF NOT EXISTS regional_schools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    subtitle VARCHAR(100),
    description TEXT,
    tags VARCHAR(500),
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 核心技法 ====================
CREATE TABLE IF NOT EXISTS techniques (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_num INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    subtitle VARCHAR(50),
    description TEXT,
    sub_techniques VARCHAR(500),
    category_tag VARCHAR(20),
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 花式动作 ====================
CREATE TABLE IF NOT EXISTS figure_moves (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_num INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    difficulty INT DEFAULT 1,
    tags VARCHAR(500)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 影像资料 ====================
CREATE TABLE IF NOT EXISTS gallery_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL COMMENT '纪录片/教学视频/活动纪实/历史照片/VR全景',
    duration VARCHAR(20),
    views INT DEFAULT 0,
    description TEXT,
    thumbnail VARCHAR(500),
    tags VARCHAR(500),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 国际交流-国家 ====================
CREATE TABLE IF NOT EXISTS intl_countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    tags VARCHAR(500),
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 国际组织 ====================
CREATE TABLE IF NOT EXISTS intl_orgs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    founded_year VARCHAR(20),
    headquarters VARCHAR(100),
    description TEXT,
    tags VARCHAR(500)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 国际交流大事记 ====================
CREATE TABLE IF NOT EXISTS intl_timeline (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year VARCHAR(10) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 团队成员 ====================
CREATE TABLE IF NOT EXISTS team_members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    role VARCHAR(100) NOT NULL,
    title VARCHAR(100),
    major VARCHAR(100),
    description TEXT,
    avatar VARCHAR(500),
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 贡献者 ====================
CREATE TABLE IF NOT EXISTS contributors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contribution_type VARCHAR(100) NOT NULL,
    description TEXT,
    sort_order INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 数据统计 ====================
CREATE TABLE IF NOT EXISTS dashboard_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stat_key VARCHAR(50) UNIQUE NOT NULL,
    stat_value VARCHAR(50) NOT NULL,
    stat_label VARCHAR(100) NOT NULL,
    sub_label VARCHAR(200),
    icon VARCHAR(50),
    color VARCHAR(20)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==================== 学习路径阶段 ====================
CREATE TABLE IF NOT EXISTS learning_stages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stage_order INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    duration VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
