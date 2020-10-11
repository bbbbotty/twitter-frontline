import time
import browser_extentions
from inspect import getmembers, isfunction
from selenium.webdriver.common.by import By
from twitter import Twitter
import os
import json
from datetime import datetime

def extend_driver(driver_class):
    for method_name, method in [o for o in getmembers(browser_extentions) if isfunction(o[1])]:
        setattr(driver_class, method_name, method)

def retweet_all(browser, urls, history_file="history.json"):
    if history_file is not None and len(history_file) > 0:
        history = {}
        if os.path.exists(history_file) and os.stat(history_file).st_size != 0:
            with open(history_file) as f:
                history = json.load(f)
            print("Loaded " + str(len(history)) + " records from history")
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
                print(f"Added new record: {url}")

            try:
                tweet = next(twitter.get_tweets())
                twitter.like_and_retweet(tweet)
                time.sleep(1)
            except: pass

    if history_file is not None and len(history_file) > 0:
        with open(history_file, "w") as f:
            json.dump(history, f, indent='\t')
