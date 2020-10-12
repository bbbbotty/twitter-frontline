# retweet.exe

## Description
Like & retweet a Twitter account. [@shiroihamusan 小白鼠先生](https://twitter.com/shiroihamusan) if not specified

### Note
It does not login to Twitter. Please use Firefox login once first.

## Usage
```
retweet.exe [-h] [--max_hours MAX_HOURS] [--min_likes MIN_LIKES] 
            [--posts_to_retweet POSTS_TO_RETWEET] [--posts_to_read POSTS_TO_READ] 
            [--headless] [url_or_file]
```
| Parameter         | Description    | Default                       |
|-------------------|----------------|------------------------------|
| --max_hours | Like & retweet the tweets in specified hours | 18    |
| --min_likes | The tweets need at least specified likes to Like & retweet | 100    |
| --posts_to_retweet | Retweet how many post to stop| 20    |
| --posts_to_read | Read how many post to stop | 50    |
| --headless | No UI |     |
| url_or_file | URL of the Twitter account | https://twitter.com/shiroihamusan    |

>

## Example
* Like & retweet Joshua Wong's Account
    * `retweet https://twitter.com/hashtag/joshuawongcf`
* Like & retweet #FridaysForFreedom tweets that are less than 48 hours with more than 10 likes
    * `retweet https://twitter.com/hashtag/FridaysForFreedom --max_hours 48 --min_likes 10`
