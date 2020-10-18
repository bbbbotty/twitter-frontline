# Install Python 3
1. Follow the instructions in <https://projects.raspberrypi.org/en/projects/generic-python-install-python3#linux> to install Python 3

# Download Source Code
1. Visit https://github.com/bbbotty/twitter-frontline/releases to download the latest release and extract the package
1. Run `git clone https://github.com/bbbotty/twitter-frontline.git` (Or use `git pull` if you already cloned it)
1. Install the dependencies `pip3 install -r requirements.txt`

# Install Firefox
1. Follow the instructions in <https://pimylifeup.com/raspberry-pi-firefox/> under the **How to Install Firefox** to install Firefox.
1. Use Raspberry PI desktop to login [Twitter](https://www.twitter.com/login) and [Telegram](https://web.telegram.org/)

# Download geckodriver
1. Currently, Raspberry PI can use the geckodriver up to v0.23 <https://github.com/mozilla/geckodriver/releases/tag/v0.23.0>
    * Direct download: <https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz>
1. Extract geckodriver into system path or the twitter-frontline directory

# Settings
`retweet.py`, `tweetall.py`, `twitterhelpbot.py` have parameters:

| Parameter         | Description    | Default                       |
|-------------------|----------------|------------------------------|
| --executable_path | Firefox executable location | `ff\App\Firefox64\firefox.exe` |
| --profile_path | Firefox User Profile location | `ff\Data\profile` |

The default values are for Forefox Portable running in Windows, please use the following values

* executable_path: `/usr/bin/firefox`
* profile_path: `/home/pi/.mozilla/firefox/xxxxx.default-esr`
    * `xxxxx` is a random number, please `ls /home/pi/.mozilla/firefox/` to see the correct directory name

Test if it runs without errors: `/path/to/firefox -P xxxxx.default-esr -headless`

## config.ini
If there is no error, update the `common` section in [config.ini](config.md)
```
[common]
executable_path=/usr/bin/firefox
profile_path=/home/pi/.mozilla/firefox/xxxxx.default-esr
headless=True
debug=False
```

# Example
```
python retweet.py
```

# VPN
You may install VPN such as NordVPN: <https://pimylifeup.com/raspberry-pi-nordvpn/>

# 注意
If you are setting up a cron job, please do not run it too frequent for
1. Twitter may identify your account as a bot account
1. `retweet.py` might take a long time to finish. You can specify a small number to `--posts_to_read` argument (Default: 40)