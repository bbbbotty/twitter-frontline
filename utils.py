import time
import browser_extentions
from inspect import getmembers, isfunction
from selenium.webdriver.common.by import By
from twitter import Twitter
import os
import json
from datetime import datetime
import sys
import signal
import configparser
import logging

logger = None

def get_logger(level=logging.INFO):
    global logger
    if logger is None:
        logger = logging.getLogger('twitter-frontline')
        logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
        logger.addHandler(ch)
    return logger

class Config(dict):
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

def read_config():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    config = Config()
    config.debug = parser.getboolean('common', 'debug', fallback=False)
    config.headless = parser.getboolean('common', 'headless', fallback=False)
    config.executable_path = parser.get('common', 'executable_path', fallback='ff\App\Firefox64\firefox.exe')
    config.profile_path = parser.get('common', 'profile_path', fallback='ff\Data\profile')
    retweet = Config()
    retweet.max_hours = parser.getint('retweet', 'max_hours', fallback=18)
    retweet.min_likes = parser.getint('retweet', 'min_likes', fallback=100)
    retweet.posts_to_retweet = parser.getint('retweet', 'posts_to_retweet', fallback=20)
    retweet.posts_to_read = parser.getint('retweet', 'posts_to_read', fallback=50)
    retweet.max_run_minutes = parser.getint('retweet', 'max_run_minutes', fallback=3)
    retweet.url_or_file = parser.get('retweet', 'url_or_file', fallback='https://twitter.com/shiroihamusan')
    twitterhelpbot = Config()
    twitterhelpbot.wait = parser.getint('twitterhelpbot', 'wait', fallback=10)
    twitterhelpbot.history = parser.get('twitterhelpbot', 'history', fallback='history.json')
    twitterhelpbot.output_file = parser.get('twitterhelpbot', 'output_file', fallback='')
    tweetall = Config()
    tweetall.history = parser.get('tweetall', 'history', fallback='history.json')
    tweetall.url_or_file = parser.get('tweetall', 'url_or_file', fallback='tweet_list.txt')
    tweetall.delete_file = parser.getboolean('tweetall', 'delete_file', fallback=False)
    config.retweet = retweet
    config.twitterhelpbot = twitterhelpbot
    config.tweetall = tweetall

    return config

def sigterm_handler(_signo, _stack_frame):
    get_logger().info("Terminated by user")
    sys.exit(0)
signal.signal(signal.SIGTERM, sigterm_handler)

def extend_driver(driver_class):
    for method_name, method in [o for o in getmembers(browser_extentions) if isfunction(o[1])]:
        setattr(driver_class, method_name, method)

def save_all(urls, save_file="tweet_list.txt"):
    if save_file is not None and len(save_file) > 0:
        with open(save_file, "a") as f:
            for url in urls:
                get_logger().info(f"Saved new record: {url}")
                f.write(url + '\n')

def retweet_all(browser, urls, history_file="history.json"):
    if history_file is not None and len(history_file) > 0:
        history = {}
        if os.path.exists(history_file) and os.stat(history_file).st_size != 0:
            with open(history_file) as f:
                history = json.load(f)
            get_logger().info(f"Loaded {len(history)} records from history")
    else:
        history = None

    twitter = Twitter(browser)
    for url in urls:
        if url not in history:
            browser.get(url)
            browser.wait(By.XPATH, ".//div[@data-testid='reply']")
            if history is not None:
                record = {}
                record["add_date"] = str(datetime.now())
                history[url] = record
                get_logger().info(f"Added new record: {url}")

            try:
                tweet = next(twitter.get_tweets())
                twitter.like_and_retweet(tweet)
                time.sleep(1)
            except: pass

    if history_file is not None and len(history_file) > 0:
        with open(history_file, "w") as f:
            json.dump(history, f, indent='\t')
