# tweetall.exe

## 做緊乜
Like & Retweet 所有响 Text file 或者網頁入面嘅 twitter links

### 注意
個 Program 唔識 Login Twitter, 個 Account 一定要用 Firefox Login 咗一次先

## 用法
```
tweetall.exe [-h] [--headless] [--delete_file] [--history] [url_or_file]
```
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| --headless | 無 UI |     |
| --delete_file | 完成 Retweet 後係咪將 `url_or_file` 刪除 |     |
| --history | 記低 Retweet 過乜，唔會再去，想不留㾗跡可以 pass 個 "" 入去 | history.json |
| url_or_file | 有 Twitter links 嘅 Text file 或者網頁 | tweet_list.txt |

>

## 例子
* Like & retweet 晒响連登嘅 Twitter links ![](images/lihkg.png)
    * `tweetall https://lihkg.com/thread/2196214/page/37`
