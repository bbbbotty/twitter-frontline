# Twitter 戰線
幾個唔同嘅 Program 去做 Twitter 任務，但記得要得閒都用個 Account 去 Post 吓自己嘢，唔係俾 Twitter 話個 Account 係 Bot 就麻煩。

## 用法

* [`retweet.exe`](retweet.md) - 就咁 Double click 就會 Like & Retweet [小白鼠先生](https://twitter.com/shiroihamusan)
* [`twitterhelperbot.exe`](twitterhelperbot.md) - 就咁 Double click 就會用 Telegram web client 解 [@TwitterHelpBot](https://t.me/TwitterHelpBot) 嘅 **香港直擊** 任務
* [`twitterall.exe`](twitterall.md) - 準備有 Twitter links 嘅 `tweet_list.txt` file, 再 Double click 就會 Like & Retweet 所有 `tweet_list.txt` 入面嘅 Twitter links

## 注意
* 每個 exe 第一次行都會問係唔係開 Firewall, 因為個 Program 同 Browser 之間係用 Network 溝通，但因為只係 localhost 行，可以㩒 Cancel
![](images/firewall.png)

## 問題
會不定時出呢個 Exception, 主要因為 Twitter 响背後 Refresh 咗，攪到 Program 有嘅 HTML element 同你見到嘅 HTML element 唔一樣，好多時再行一次個 Program 就 OK.
```
 Traceback (most recent call last):
  File "retweet.py", line 37, in <module>
  File "twitter.py", line 104, in get_tweets
  File "browser_extentions.py", line 10, in scroll_to_element
  File "site-packages\selenium\webdriver\remote\webdriver.py", line 634, in execute_script
  File "site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
  File "site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
selenium.common.exceptions.StaleElementReferenceException: Message: The element reference of <div class="css-1dbjc4n r-18u37iz"> is stale; either the element is no longer attached to the DOM, it is not in the current frame context, or the document has been refreshed
```