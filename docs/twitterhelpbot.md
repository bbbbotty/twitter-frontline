# twitterhelpbot.exe

## 做緊乜
用 Telegram web client 解 [@TwitterHelpBot](https://t.me/TwitterHelpBot) **香港直擊**, **國際戰線**, 同 **外語新聞** 任務

### 注意
1. 個 Program 唔識 Login Telegram 同 Twitter, 兩個 Account 一定要用 Firefox Login 咗一次先
1. Telegram account 必須已經加咗 [@TwitterHelpBot](https://t.me/TwitterHelpBot)
1. 個 Program 唔會㩒 **完成任務**

## 用法
```
twitterhelpbot.exe [-h] [--wait WAIT] [--continuation] [--headless] [--history]
```
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| --wait | 等幾多秒 Telegram Web Client Ready | 10    |
| --continuation | 繼續之前嘅任務 | |
| --headless | 無 UI |     |
| --history | 記低 Retweet 過乜，唔會再去，想不留㾗跡可以 pass 個 "" 入去 | history.json |

>

## 例子
* Telegram Web Client 有時要等好耐先 Ready, 可以 Set 做等兩分鐘
    * `twitterhelpbot --wait 120`
* 如果之前個任務未做完就熄咗，可以加個 --continuation, 就唔會再入 /task, 直接拎上次嘅任務做嘢
    * `twitterhelpbot --continuation`
