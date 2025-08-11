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

更多詳情，請參閱 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 遊戲玩法

1. 運行遊戲：
```
python snake_game.py
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
snake/
│── snake_game.py       # 遊戲主文件
│── assets/             # 遊戲資源（圖片、聲音）
├── Document/           # 其餘文檔
│   ├── README/         # 其餘 README 文檔
│   │   ├── zh_cn.md    # 中文
│   │   ├── zh_tw.md    # 繁体
│── LICENSE             # GPL-3.0 許可證
│── README.md           # 本自述文件
│── CONTRIBUTING.md     # 本貢獻文件
└── requirements.txt    # 專案依賴項
```

## 貢獻

歡迎貢獻！如果您有任何改進或錯誤修復的想法，請：

1. fork 程式碼庫
2. 建立您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some awesome feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交拉取請求

## 許可證

本項目遵循 GPL-3.0 許可證 - 詳情請參閱[License here](./LICENSE)

## 致謝

- 感謝 Pygame 社區，感謝他們提供優秀的遊戲開發庫
- 感謝經典貪食蛇遊戲的創作者，感謝他們最初的構思
- 所有幫助改進本計畫的貢獻者