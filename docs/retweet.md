# retweet.exe

## 做緊乜
Like & retweet 一個 Twitter Account. 無 specific 嘅話會 like & retweet 小白鼠先生嘅 account

### 注意
個 Program 唔識 Login Twitter, 個 Account 一定要用 Firefox Login 咗一次先

## 用法
```
retweet.exe [-h] [--max_hours MAX_HOURS] [--min_likes MIN_LIKES] [--max_run_minutes MAX_RUN_MINUTES]
            [--posts_to_retweet POSTS_TO_RETWEET] [--posts_to_read POSTS_TO_READ] 
            [--headless] [url_or_file]
```
| 參數        | 咩嚟                               | 預設值 |
|-------------|-----------------------------------|--------|
| --max_hours | Like & retweet 幾多個鐘頭內嘅 Tweet | 18    |
| --min_likes | 條 Tweet 最少要有幾多 Likes 先會 Like & retweet | 100    |
| --max_run_minutes | Program 幾多行幾耐 | 3    |
| --posts_to_retweet | 要 Retweet 幾多條先停 | 20    |
| --posts_to_read | 要碌過幾多條 Tweet 先停 | 50    |
| --headless | 無 UI |     |
| url_or_file | Twitter account 嘅網址 | https://twitter.com/shiroihamusan    |

>

## 例子
* Like & retweet 黃之峰嘅 Account
    * `retweet https://twitter.com/hashtag/joshuawongcf`
* Like & retweet 48個鐘頭內有多過10個 Like 嘅 #FridaysForFreedom tweet
    * `retweet https://twitter.com/hashtag/FridaysForFreedom --max_hours 48 --min_likes 10`
