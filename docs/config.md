# config.ini
Where the default values located. Command-line parameter, exists, will override the settings.

## Availability
v1.0.3 or above

# [common]
| Parameter         | Description    | Default                       |
|-------------------|----------------|------------------------------|
| executable_path | Firefox executable location | `ff\App\Firefox64\firefox.exe` |
| profile_path | Firefox User Profile location | `ff\Data\profile` |
| headless | No UI |     |
| debug | Show debug information |     |

>

# [retweet]
| Parameter   | Description                       | Default |
|-------------|-----------------------------------|---------|
| max_hours | Like & retweet the tweets in specified hours | 18    |
| min_likes | The tweets need at least specified likes to Like & retweet | 100    |
| max_run_minutes | How long can the program run (in minutes)| 3    |
| posts_to_retweet | Retweet how many post to stop| 20    |
| posts_to_read | Read how many post to stop | 50    |
| url_or_file | URL of the Twitter account | https://twitter.com/shiroihamusan    |

>

# [tweetall]
| Parameter   | Description                       | Default |
|-------------|-----------------------------------|---------|
| delete_file | Delete `url_or_file` after retweet |     |
| history | Save the retweet URLs to prevent revisiting. Use empty value (`history=`) if no history desired | history.json |
| url_or_file | File or web page listed the tweets | tweet_list.txt |

>

# [twitterhelpbot]
| Parameter   | Description                       | Default |
|-------------|-----------------------------------|---------|
| wait | How long to wait for Telegram Web Client getting ready (seconds) | 10    |
| history | Save the retweet URLs to prevent revisiting. Use empty value (`history=`) if no history desired | history.json |
| output_file | Will not retweet immediately. It saves the links into a file for tweetall to retweet | tweet_list.txt |

>

# Example
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