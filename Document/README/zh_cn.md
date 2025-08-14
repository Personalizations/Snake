# Python 贪吃蛇游戏

一款使用 Python 和 Pygame 库实现的经典贪吃蛇游戏。控制贪吃蛇进食、变长，并避免与墙壁或自身碰撞。

## 功能

- 经典贪吃蛇游戏机制
- 得分追踪系统
- 随着贪吃蛇的成长，难度逐渐增加
- 游戏结束检测
- 简单直观的操作方式
- 色彩丰富的画面

## 要求

- Python 3.6 或更高版本
- Pygame 库

## 安装

更多详情，请参阅 [CONTRIBUTING.md](../CONTRIBUTING/zh_cn.md)。

## 游戏玩法

1. 运行游戏：
```
python snake_game.py
```

2. 使用方向键控制蛇的方向：
- 向上键：向上移动
- 向下键：向下移动
- 向左键：向左移动
- 向右键：向右移动

3. 吃掉红色食物来变长并增加分数
4. 避免撞到墙壁或蛇自身的身体
5. 随时按“Q”键退出游戏
6. 游戏结束后按“R”键重新开始

## 游戏机制

- 蛇会沿着其面向的方向持续移动
- 每次吃掉食物，蛇都会变长一段
- 每吃掉一个食物，分数增加 10 分
- 游戏速度随着蛇的生长而逐渐加快
- 如果蛇撞到墙壁或自身的身体，游戏就会结束

## 项目结构

```
snake/
├── snake_game.py       # 游戏主文件
├── assets/             # 游戏资源（图片、声音）
├── Document/           # 文档目录
│  ├── README/          # 多语言README文档
│  │  ├── zh_cn.md      # 简体中文README
│  │  ├── zh_tw.md      # 繁体中文README
│  │  └── jp.md         # 日语README
│  └── CONTRIBUTING/    # 多语言贡献指南
│     ├── zh_cn.md      # 简体中文贡献指南
│     ├── zh_tw.md      # 繁体中文贡献指南
│     └── jp.md         # 日语贡献指南
├── LICENSE             # GPL-3.0 许可证
├── README.md           # 主README文件（英文）
├── CONTRIBUTING.md     # 主贡献指南文件（英文）
├── Changelog.md        # 更新日志文件
├── requirements.txt    # 项目依赖项
└── .idea/              # IDE配置文件
    ├── vcs.xml         # 版本控制配置
    ├── modules.xml     # 模块配置
    ├── .gitignore      # IDE特定忽略文件
    ├── jsLibraryMappings.xml  # JavaScript库映射
    ├── inspectionProfiles/    # 检查配置文件
    │  └── Project_Default.xml # 默认项目检查配置
    └── misc.xml        # 其他杂项配置
```

## 贡献

欢迎贡献！如果您有任何改进或错误修复的想法，请：

1. fork 代码库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some awesome feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交拉取请求

## 许可证

本项目遵循 GPL-3.0 许可证 - 详情请参阅[License here](../../LICENSE)

## 致谢

- 感谢 Pygame 社区，感谢他们提供优秀的游戏开发库
- 感谢经典贪吃蛇游戏的创作者，感谢他们最初的构思
- 所有帮助改进本项目的贡献者