# twitterhelpbot.exe

## Description
Use Telegram web client to like and retweets [@TwitterHelpBot](https://t.me/TwitterHelpBot)'s tasks

### Note
1. It does not login to Telegram and Twitter. Please use Firefox login once first.
1. Telegram account shall already added [@TwitterHelpBot](https://t.me/TwitterHelpBot)
1. It does not press **完成任務** button

## Usage
```
twitterhelpbot.exe [-h] [--wait WAIT] [--continuation] [--headless] [--history] [--output_file]
```
| Parameter         | Description    | Default                       |
|-------------|-----------------------------------|--------|
| --wait | How long to wait for Telegram Web Client getting ready (seconds) | 10    |
| --continuation | Continue previous tasks | |
| --headless | No UI |     |
| --history | Save the retweet URLs to prevent revisiting. Use "" if no history desired | history.json |
| --output_file | Will not retweet immediately. It saves the links into a file for tweetall to retweet | tweet_list.txt |

>

## Example
* Sometimes, Telegram Web Client might take a long time to get ready. We can set it to wait for 2 minutes
    * `twitterhelpbot --wait 120`
* If the previous execution was halt, using --continuation will not enter /task to query the tasks again
    * `twitterhelpbot --continuation`
