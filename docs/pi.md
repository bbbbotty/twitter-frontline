# 裝 Python 3
1. 跟住 <https://projects.raspberrypi.org/en/projects/generic-python-install-python3#linux> 去裝 Python 3

# Download Twitter戰線 Source Code
1. 去 https://github.com/bbbotty/twitter-frontline/releases Download 最新 Release, 再 Extract 個 Package
1. 或者 git clone https://github.com/bbbotty/twitter-frontline.git (如果之前已經 clone 咗，用 git pull)
1. 行 `pip3 install -r requirements.txt`

# 裝 Firefox
1. 跟住 <https://pimylifeup.com/raspberry-pi-firefox/> 嘅 **How to Install Firefox** 去裝 Firefox.
1. 用 Raspberry PI desktop 去 login [Twitter](https://www.twitter.com/login) 同 [Telegram](https://web.telegram.org/)

# Download geckodriver
1. 暫時 Raspberry PI 用到 geckodriver 嘅最新片本係 v0.23 <https://github.com/mozilla/geckodriver/releases/tag/v0.23.0>
    * 直接 Download: <https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz>
1. Extract 完將 geckodriver 放响 path 或者 twitter-frontline 嘅 directory

# 設定
`retweet.py`, `tweetall.py`, `twitterhelpbot.py` 都會食兩個 parameters:

| 參數              | 咩嚟            | 預設值                       |
|-------------------|----------------|------------------------------|
| --executable_path | Firefox 嘅話置 | `ff\App\Firefox64\firefox.exe` |
| --profile_path | Firefox User Profile 嘅位置 | `ff\Data\profile` |

因為預設值係俾 Windows 行 Firefox Portable, 所以指住一條 relative path, 要代入返相應參數

* executable_path: `/usr/bin/firefox`
* profile_path: `/home/pi/.mozilla/firefox/xxxxx.default-esr`
    * `xxxxx` 係亂數，要用 `ls /home/pi/.mozilla/firefox/` 睇返

可以試吓行呢句去睇吓有無 Error: `/path/to/firefox -P xxxxx.default-esr -headless`

## config.ini
無 Error 嘅話就可以改 [config.ini](config.md) 嘅 `common` section
```
[common]
executable_path=/usr/bin/firefox
profile_path=/home/pi/.mozilla/firefox/xxxxx.default-esr
headless=True
debug=False
```

# 執行示範
```
python retweet.py –-executable_path /usr/bin/firefox –-profile_path /home/pi/.mozilla/firefox/xxxxx.default-esr --headless
```

# VPN
可以裝埋 VPN, 例如 NordVPN: <https://pimylifeup.com/raspberry-pi-nordvpn/>

# 注意
如果要 set cron job 自己行，唔好 set 得太密，一來有機會俾 Twitter 當個 Account 係 Bot, 二來 `retweet.py` 有機會 Loop 死, 可以加返個 `--posts_to_read` 去 set 細少少解決 (Default: 40)