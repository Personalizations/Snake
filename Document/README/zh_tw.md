# Python 貪吃蛇遊戲

一款使用 Python 和 Pygame 函式庫實現的經典貪吃蛇遊戲。控制貪吃蛇進食、變長，並避免與牆壁或自身碰撞。

## 功能

- 經典貪吃蛇遊戲機制
- 得分追蹤系統
- 隨著貪吃蛇的成長，難度逐漸增加
- 遊戲結束檢測
- 簡單直覺的操作方式
- 色彩豐富的畫面

## 要求

- Python 3.6 或更高版本
- Pygame 庫

## 安裝

更多詳情，請參閱 [CONTRIBUTING.md](../CONTRIBUTING/zh_tw.md)。

## 遊戲玩法

1. 運行遊戲：
   ```
   python main.py
   ```

2. 使用方向鍵控制蛇的方向：
  - 向上鍵：向上移動
  - 向下鍵：向下移動
  - 向左鍵：向左移動
  - 向右鍵：向右移動

3. 吃掉紅色食物變長並增加分數
4. 避免撞到牆壁或蛇自身的身體
5. 隨時按「Q」鍵退出遊戲
6. 遊戲結束後按下「R」鍵重新開始

## 遊戲機制

- 蛇會沿著其面向的方向持續移動
- 每次吃掉食物，蛇就會變長一段
- 每吃掉一個食物，分數增加 10 分
- 遊戲速度隨著蛇的生長而逐漸加快
- 如果蛇撞到牆壁或自身的身體，遊戲就會結束

## 專案結構

```
Snake/                     # 項目根目錄，整體是一個貪吃蛇遊戲項目
├── CHANGELOG.md            # 項目更新日誌，記錄各版本的功能變更和修復內容
├── CONTRIBUTING.md         # 貢獻指南，指導開發者如何參與項目貢獻
├── LICENSE                 # 項目許可證文件，規定項目的使用權限和限制
├── README.md               # 項目主要說明文件，包含項目介紹、安裝和使用方法等
├── main.py                 # 程序主要入口文件，負責啟動遊戲和統籌各模組
├── requirements.txt        # 項目依賴清單，記錄運行所需的Python庫及版本
├── tree.py                 # 專案架構生成腳本
├── .idea/                  # PyCharm IDE的項目配置目錄
│   ├── Snake.iml           # 項目模組配置文件
│   ├── jsLibraryMappings.xml # JavaScript庫映射配置
│   ├── misc.xml            # 雜項配置
│   ├── modules.xml         # 模組結構配置
│   ├── vcs.xml             # 版本控制系統配置
│   ├── workspace.xml       # 工作區配置，記錄IDE的窗口布局等
│   ├── inspectionProfiles/ # 代碼檢查配置文件目錄
│   │   ├── Project_Default.xml # 默認項目檢查配置
│   │   ├── profiles_settings.xml # 檢查配置文件的設置
├── Assets/                 # 遊戲資源目錄，存放各類素材
│   ├── index.html          # 可能是遊戲的網頁說明或配套網頁界面
│   ├── audio/              # 音頻資源目錄
│   │   ├── home_menu/      # 主菜單相關音效
│   │   │   ├── confirm.wav # 確認操作音效
│   │   │   ├── select.wav  # 選擇操作音效
│   ├── background/         # 背景圖片目錄
│   │   ├── home_menu/      # 主菜單背景圖片
│   │   │   ├── menu_cn.png # 中文菜單背景
│   │   │   ├── menu_en.png # 英文菜單背景
│   │   │   ├── menu_jp.png # 日文菜單背景
│   │   │   ├── menu_zh_tw.png # 繁體中文菜單背景
│   ├── icon/               # 圖標資源目錄
│   │   ├── test.txt        # 圖標資源測試文件（可能用於記錄圖標相關信息）
├── Document/               # 項目文檔目錄，包含多語言文檔
│   ├── CONTRIBUTING/       # 多語言貢獻指南
│   │   ├── jp.md           # 日文貢獻指南
│   │   ├── zh_cn.md        # 中文（簡體）貢獻指南
│   │   ├── zh_tw.md        # 中文（繁體）貢獻指南
│   ├── README/             # 多語言說明文檔
│   │   ├── jp.md           # 日文說明文檔
│   │   ├── zh_cn.md        # 中文（簡體）說明文檔
│   │   ├── zh_tw.md        # 中文（繁體）說明文檔
├── Function/               # 遊戲功能模組目錄
│   ├── game/               # 遊戲核心功能目錄
│   │   ├── game_core.py    # 遊戲核心邏輯實現（如蛇的移動、碰撞檢測等）
│   ├── home_menu/          # 主菜單功能目錄
│   │   ├── exit_game.py    # 退出遊戲功能實現
│   │   ├── menu_controls.py # 菜單控制邏輯（如導航、選擇等）
│   │   ├── options.py      # 遊戲選項設置功能（如音效、語言等）
│   │   ├── start_game.py   # 啟動遊戲功能實現，負責從菜單進入遊戲
```

## 貢獻

歡迎貢獻！如果您有任何改進或錯誤修復的想法，請：

1. fork 程式碼庫
2. 建立您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some awesome feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交拉取請求

## 許可證

本項目遵循 GPL-3.0 許可證 - 詳情請參閱[License here](../../LICENSE)

## 致謝

- 感謝 Pygame 社區，感謝他們提供優秀的遊戲開發庫
- 感謝經典貪食蛇遊戲的創作者，感謝他們最初的構思
- 所有幫助改進本計畫的貢獻者