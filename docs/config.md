# config.ini
放置預設值嘅地方，如果有 command-line parameter, command-line parameter 優先

## 適用版本
v1.0.3 或以上

# [common]
| 參數              | 咩嚟            | 預設值                       |
|-------------------|----------------|------------------------------|
| executable_path | Firefox 嘅話置 | ff\App\Firefox64\firefox.exe |
| profile_path | Firefox User Profile 嘅位置 | ff\Data\profile |
| headless | 無 UI |     |
| debug | 顯示 debug 資訊 |     |

>

# [retweet]
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| max_hours | Like & retweet 幾多個鐘頭內嘅 Tweet | 18    |
| min_likes | 條 Tweet 最少要有幾多 Likes 先會 Like & retweet | 100    |
| max_run_minutes | Program 最多行幾多分鐘 | 3    |
| posts_to_retweet | 要 Retweet 幾多條先停 | 20    |
| posts_to_read | 要碌過幾多條 Tweet 先停 | 50    |
| url_or_file | Twitter account 嘅網址 | https://twitter.com/shiroihamusan    |

>

# [tweetall]
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| delete_file | 完成 Retweet 後係咪將 `url_or_file` 刪除 |     |
| history | 記低 Retweet 過乜，唔會再去，想不留㾗跡可以 pass 個 "" 入去 | history.json |
| url_or_file | 有 Twitter links 嘅 Text file 或者網頁 | tweet_list.txt |

>

# [twitterhelpbot]
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| wait | 等幾多秒 Telegram Web Client Ready | 10    |
| history | 記低 Retweet 過乜，唔會再去，想不留㾗跡可以 pass 個 "" 入去 | history.json |
| output_file | 唔即時 retweet, save 落個 file 度可以俾 tweetall 去 retweet | tweet_list.txt |

>

# [範例]
```
[common]
executable_path=ff\App\Firefox64\firefox.exe
profile_path=ff\Data\profile
headless=False
debug=False

[retweet]
max_hours=18
min_likes=100
max_run_minutes=3
posts_to_retweet=20
posts_to_read=50
url_or_file=https://twitter.com/shiroihamusan

[tweetall]
history=history.json
delete_file=False
url_or_file=tweet_list.txt

[twitterhelpbot]
wait=10
history=history.json
output_file=tweet_list.txt
```