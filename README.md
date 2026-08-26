[README.md](https://github.com/user-attachments/files/31473631/README.md)
<div align="center">

# 中国空竹非遗数据库系统

**Kongzhu (Diabolo) Intangible Cultural Heritage Database**

探索千年非遗文化，传承中华空竹技艺

![License](https://img.shields.io/badge/License-Proprietary-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.1-black)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-06B6D4)
![Database](https://img.shields.io/badge/Database-SQLite%20%2F%20MySQL-orange)

</div>

---

## 📖 项目简介

抖空竹是中国传统体育游艺的杰出代表，2006 年经国务院批准列入**第一批国家级非物质文化遗产名录（编号：VI-4）**。然而，随着现代化进程的加速，空竹非遗正面临传承人老龄化、青年传承断层、原生技艺资料加速流失、大众认知度不足等多重危机。

在这一背景下，烟台南山学院 **"抖趣竹风"大学生创新创业团队**（2023 年成立，由市级抖空竹代表性传承人杨文哲担任负责人）聚焦 **"数字化记录 + 体验式传播 + 商业化转化"** 三位一体模式，倾力打造 **中国空竹非遗数据库系统**，旨在通过数字技术手段推动空竹非遗的活态传承与创新发展，让濒临失传的抖空竹非遗走进年轻一代的日常生活。

---

## ✨ 核心功能

### 六大核心模块

| 模块 | 说明 |
| --- | --- |
| 📜 **政策知识** | 国家级非遗保护政策法规、地方空竹文化发展计划、非遗法解读与学术研究成果 |
| 👤 **传承人物** | 国家级、省级、市级抖空竹代表性传承人档案，涵盖传承谱系、技艺特点、教学成果与获奖荣誉 |
| 📰 **活动新闻** | 国内外空竹文化活动、赛事新闻、学术交流、校园美育与公益支教等最新动态 |
| 🎓 **学习课程** | 全年龄段阶梯式教学课程，含零基础入门、中级进阶、高级表演及"扬竹康养十式"专项课程 |
| 🏆 **竞赛信息** | 全国锦标赛、国际赛事、地方艺术节等竞赛日历、报名指南、获奖数据统计与赛事规则 |
| 🛍 **文创产品** | 空竹国潮文创、传统工艺套装、非遗衍生品及教学图书，推动空竹文化产业化发展 |

### 拓展模块

- 📚 **历史渊源** —— 三国至现代空竹历史大事年表、名称演变、地域流派
- 🎯 **技艺技法** —— 六大核心技法（抖、捞、盘、绕、抛、接）与 200 余种花式动作图谱
- 🎬 **影像资料** —— 纪录片、教学视频、活动纪实、VR 全景等多媒体资源
- 🌏 **国际交流** —— 覆盖 18 个国家的传播版图、国际组织与交流大事记
- 📊 **数据统计** —— 数据库全景统计、数据增长趋势可视化（Chart.js）
- 👥 **关于我们** —— 项目背景、核心团队、"一赋三守一融新"体系与知识产权声明

### "一赋三守一融新"体系

| 维度 | 内涵 |
| --- | --- |
| **一赋** | 数字化赋能 —— 搭建空竹非遗数据库，完成技艺数字化记录与留存 |
| **守技** | 守技艺之本 —— 完整记录传承六大核心技法与经典花式动作 |
| **守人** | 守传承之人 —— 建立传承人档案，培养新一代青年空竹传承力量 |
| **守物** | 守文化之物 —— 收集保护传统空竹实物、文献资料和历史影像 |
| **融新** | 融合创新 —— VR/AI 教学、国潮文创、康养课程等多元化创新发展 |

---

## 📊 数据库全景统计

| 收录传承人 | 政策文献条目 | 教学课程 | 活动新闻记录 | 影像视频资源 | 文创产品 | 国际覆盖国家 | 标准动作收录 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **32** | **156** | **48** | **260+** | **86** | **28** | **18** | **200** |
| 国家级5 · 省级12 · 市级15 | 国家级26 · 地方级98 · 学术32 | 入门12 · 中级18 · 高级10 · 专项8 | 文化节 · 校园 · 国际 · 社区 · 公益 | 纪录片 · 教学片 · 活动纪实 · VR | 传统工艺 · 国潮 · 图书 · 智能 | 亚洲 · 欧洲 · 北美洲 · 大洋洲 | 六大技法 · 花式图谱 · 教学分解 |

---

## 🛠 技术栈

### 前端
- **HTML5 / Tailwind CSS** —— 响应式布局，适配 PC、平板、手机多终端
- **Chart.js** —— 数据可视化图表
- **Font Awesome** —— 图标库
- **ZCOOL 站酷字体** —— 中国风视觉设计（红金蓝三色体系）

### 后端
- **Python 3.8+** + **Flask 3.1.1** —— Web 框架
- **Flask-SQLAlchemy** —— ORM 数据模型
- **Flask-CORS** —— 跨域支持
- **SQLite / MySQL** —— 数据库（默认 SQLite，支持切换 MySQL）

---

## 📁 项目结构

```
空竹数据库/
├── index.html              # 首页（英雄区、功能导航、数据统计）
├── policy.html             # 政策知识
├── heritage.html           # 传承人物
├── activities.html         # 活动新闻
├── courses.html            # 学习课程
├── competition.html        # 竞赛信息
├── products.html           # 文创产品
├── history.html            # 历史渊源
├── technique.html          # 技艺技法
├── gallery.html            # 影像资料
├── international.html      # 国际交流
├── database.html           # 数据统计与使用指南
├── about.html              # 关于我们
└── backend/                # Flask 后端
    ├── app.py              # 应用工厂与入口
    ├── config.py           # 配置（数据库连接、密钥等）
    ├── models.py           # SQLAlchemy 数据模型（20+ 张表）
    ├── init_db.sql         # MySQL 建表脚本
    ├── seed_data.py        # 种子数据填充脚本
    ├── requirements.txt    # 依赖清单
    ├── kongzhu.db          # SQLite 数据库文件
    └── routes/             # API 路由（按模块拆分）
        ├── policy.py       ├── heritage.py    ├── activity.py
        ├── course.py       ├── competition.py ├── product.py
        ├── history.py      ├── technique.py   ├── gallery.py
        ├── international.py├── statistics.py  └── about.py
```

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip

### 后端启动

```bash
# 1. 进入后端目录
cd backend

# 2. 安装依赖
pip install -r requirements.txt

# 3.（可选）填充种子数据
python seed_data.py

# 4. 启动服务（默认 http://localhost:5000）
python app.py
```

### 前端访问

前端页面为纯静态 HTML，可直接在浏览器中打开，或通过任意静态服务器托管：

```bash
# 使用 Python 内置服务器
python -m http.server 8080
```

浏览器访问 `http://localhost:8080` 即可。

> 💡 后端默认使用 SQLite（`backend/kongzhu.db`），无需额外配置。如需切换 MySQL，请先执行 `backend/init_db.sql` 建库，并修改 `backend/config.py` 中的 `SQLALCHEMY_DATABASE_URI`。

---

## 🔌 API 接口

统一响应格式：

```json
{ "code": 200, "data": ..., "message": "..." }
```

| 模块 | 前缀 | 主要接口 |
| --- | --- | --- |
| 政策知识 | `/api/policies` | `GET /` `GET /<id>` `POST /` `PUT /<id>` `DELETE /<id>` `GET /levels` |
| 传承人物 | `/api/heritage` | `/inheritors` `/orgs` `/stats` |
| 活动新闻 | `/api/activities` | `GET /` `GET /<id>` `GET /categories` `POST/PUT/DELETE` |
| 学习课程 | `/api/courses` | `GET /` `GET /<id>` `GET /kangyang` `GET /stages` |
| 竞赛信息 | `/api/competitions` | `GET /` `GET /<id>` `GET /awards` |
| 文创产品 | `/api/products` | `GET /` `GET /<id>` `GET /categories` |
| 历史渊源 | `/api/history` | `/events` `/names` `/schools` |
| 技艺技法 | `/api/techniques` | `/core` `/moves` |
| 影像资料 | `/api/gallery` | `/items` `/items/<id>` `/categories` |
| 国际交流 | `/api/international` | `/countries` `/orgs` `/timeline` |
| 数据统计 | `/api/statistics` | `/dashboard` `/totals` `/growth` |
| 关于我们 | `/api/about` | `/team` `/contributors` |
| 健康检查 | `/api/health` | `GET /api/health` |

---

## 🗄 数据库设计

系统基于 SQLAlchemy 定义 20+ 张数据表，核心表结构如下（MySQL 脚本见 `backend/init_db.sql`）：

- `policies` —— 政策文献
- `inheritors` —— 传承人物
- `heritage_orgs` —— 传承组织
- `inheritor_stats` —— 传承人层级统计
- `activities` —— 活动新闻
- `courses` —— 学习课程
- `kangyang_styles` —— 扬竹康养十式
- `learning_stages` —— 学习路径阶段
- `competitions` —— 竞赛信息
- `awards` —— 竞赛获奖记录
- `products` —— 文创产品
- `history_events` —— 历史大事年表
- `name_evolutions` —— 空竹名称演变
- `regional_schools` —— 地域流派
- `techniques` —— 核心技法
- `figure_moves` —— 花式动作
- `gallery_items` —— 影像资料
- `intl_countries` / `intl_orgs` / `intl_timeline` —— 国际交流
- `team_members` —— 团队成员
- `contributors` —— 贡献者
- `dashboard_stats` —— 数据统计概览

---

## 👥 核心团队

| 姓名 | 角色 | 简介 |
| --- | --- | --- |
| **杨文哲** | 项目负责人 | 市级抖空竹代表性传承人，自幼习练空竹，精通六大核心技法和 50 余种花式动作 |
| **李明远** | 技术负责人 | 计算机科学与技术专业，负责数据库系统架构设计、前端开发及 VR/AI 平台研发 |
| **王晓雨** | 运营负责人 | 文化产业管理专业，负责全媒体传播、文创设计与文旅研学项目运营 |

## 🤝 内容贡献者

| 姓名/单位 | 贡献类型 | 说明 |
| --- | --- | --- |
| 杨文哲 | 技艺资料 | 核心技法动作演示与课程体系设计 |
| 张国良 | 口述历史 | 40 年空竹传承经历的口述史资料 |
| 烟台南山学院 | 平台支持 | 非遗工坊场地、数据库服务器与技术研发支持 |
| 李明远 | 系统开发 | 数据库系统架构设计与前端开发 |
| 王晓雨 | 内容编辑 | 政策文献整理、活动新闻采编与产品信息录入 |
| 中国非遗保护中心 | 学术支持 | 空竹非遗保护政策文献与学术研究成果 |

---

## ⚖️ 知识产权声明

中国空竹数据库系统由烟台南山学院"抖趣竹风"大学生创新创业团队独立设计、开发和运营，以下知识产权内容受中华人民共和国相关法律法规保护：

- **软件著作权** —— 源代码、数据库架构、页面布局和交互设计
- **课程著作权** —— "扬竹康养十式"课程体系及其配套教学资料
- **商标权** —— "抖趣竹风""扬竹康养"等品牌名称和标识
- **数据所有权** —— 传承人档案、技艺动作数据、政策文献摘编等汇编著作权
- **专利权** —— 智能空竹硬件产品的传感器集成方案和结构设计

> 未经烟台南山学院"抖趣竹风"团队书面授权，任何单位和个人不得对本系统进行复制、修改、反向工程、数据抓取或商业性使用。

---

## 📄 许可证

本项目为**专有软件（Proprietary）**，未授权不得复制、分发或商业使用。转载引用请注明来源"中国空竹数据库系统"。

---

## 📮 联系我们

- **地址**：山东省XXXXXXXXXXXXXX学院
- **电话**：0535-1234567
- **邮箱**：douquzhufeng@example.com

### 合作伙伴

中国非遗保护中心 · 烟台南山学院 · 全国空竹协会 · 非遗文化基金会

---

<div align="center">

&copy; 2026 中国空竹数据库系统. 保留所有权利.

</div>
