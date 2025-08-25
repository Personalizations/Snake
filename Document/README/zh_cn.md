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
   python main.py
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
7. 随时按“ESC”键退出当前页面

## 游戏机制

- 蛇会沿着其面向的方向持续移动
- 每次吃掉食物，蛇都会变长一段
- 每吃掉一个食物，分数增加 10 分
- 游戏速度随着蛇的生长而逐渐加快
- 如果蛇撞到墙壁或自身的身体，游戏就会结束

## 项目结构

```
Snake/                     # 项目根目录，整体是一个贪吃蛇游戏项目
├── CHANGELOG.md            # 项目更新日志，记录各版本的功能变更和修复内容
├── CONTRIBUTING.md         # 贡献指南，指导开发者如何参与项目贡献
├── LICENSE                 # 项目许可证文件，规定项目的使用权限和限制
├── README.md               # 项目主说明文档，包含项目介绍、安装和使用方法等
├── main.py                 # 程序主入口文件，负责启动游戏和统筹各模块
├── requirements.txt        # 项目依赖清单，记录运行所需的Python库及版本
├── tree.py                 # 项目架构生成脚本
├── .idea/                  # PyCharm IDE的项目配置目录
│   ├── Snake.iml           # 项目模块配置文件
│   ├── jsLibraryMappings.xml # JavaScript库映射配置
│   ├── misc.xml            # 杂项配置
│   ├── modules.xml         # 模块结构配置
│   ├── vcs.xml             # 版本控制系统配置
│   ├── workspace.xml       # 工作区配置，记录IDE的窗口布局等
│   ├── inspectionProfiles/ # 代码检查配置文件目录
│   │   ├── Project_Default.xml # 默认项目检查配置
│   │   ├── profiles_settings.xml # 检查配置文件的设置
├── Assets/                 # 游戏资源目录，存放各类素材
│   ├── index.html          # 可能是游戏的网页说明或配套网页界面
│   ├── audio/              # 音频资源目录
│   │   ├── home_menu/      # 主菜单相关音效
│   │   │   ├── confirm.wav # 确认操作音效
│   │   │   ├── select.wav  # 选择操作音效
│   ├── background/         # 背景图片目录
│   │   ├── home_menu/      # 主菜单背景图片
│   │   │   ├── menu_cn.png # 中文菜单背景
│   │   │   ├── menu_en.png # 英文菜单背景
│   │   │   ├── menu_jp.png # 日文菜单背景
│   │   │   ├── menu_zh_tw.png # 繁体中文菜单背景
│   ├── icon/               # 图标资源目录
│   │   ├── test.txt        # 图标资源测试文件（可能用于记录图标相关信息）
├── Document/               # 项目文档目录，包含多语言文档
│   ├── CONTRIBUTING/       # 多语言贡献指南
│   │   ├── jp.md           # 日文贡献指南
│   │   ├── zh_cn.md        # 中文（简体）贡献指南
│   │   ├── zh_tw.md        # 中文（繁体）贡献指南
│   ├── README/             # 多语言说明文档
│   │   ├── jp.md           # 日文说明文档
│   │   ├── zh_cn.md        # 中文（简体）说明文档
│   │   ├── zh_tw.md        # 中文（繁体）说明文档
├── Function/               # 游戏功能模块目录
│   ├── game/               # 游戏核心功能目录
│   │   ├── game_core.py    # 游戏核心逻辑实现（如蛇的移动、碰撞检测等）
│   ├── home_menu/          # 主菜单功能目录
│   │   ├── exit_game.py    # 退出游戏功能实现
│   │   ├── menu_controls.py # 菜单控制逻辑（如导航、选择等）
│   │   ├── options.py      # 游戏选项设置功能（如音效、语言等）
│   │   ├── start_game.py   # 启动游戏功能实现，负责从菜单进入游戏
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