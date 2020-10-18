import time
from datetime import datetime
import os
from ff import init as browser_init
from twitter import Twitter
import argparse
from selenium.webdriver.common.by import By
import logging
import utils

if __name__ == "__main__":

    config = utils.read_config()

    parser = argparse.ArgumentParser(description='Retweet a specific page')
    parser.add_argument('url_or_file', nargs='?', default=config.retweet.url_or_file)
    parser.add_argument('--max_hours', default=config.retweet.max_hours, type=int)
    parser.add_argument('--min_likes', default=config.retweet.min_likes, type=int)
    parser.add_argument('--max_run_minutes', default=config.retweet.max_run_minutes, type=int)
    parser.add_argument('--posts_to_retweet', default=config.retweet.posts_to_retweet, type=int)
    parser.add_argument('--posts_to_read', default=config.retweet.posts_to_read, type=int)
    parser.add_argument('--executable_path', default=config.executable_path)
    parser.add_argument('--profile_path', default=config.profile_path)
    parser.add_argument('--headless', action='store_true', default=config.headless)
    parser.add_argument('--debug', action='store_true', default=config.debug)

    args = parser.parse_args()

    logger = utils.get_logger(logging.INFO if not args.debug else logging.DEBUG)

    urls = [args.url_or_file]
    if os.path.exists(args.url_or_file):
        with open(args.url_or_file, newline="", encoding="utf-8") as f:
            urls = [url.strip() for url in f if len(url.strip()) > 0]
    
    logger.info("start ")

    with browser_init(executable_path=args.executable_path, profile_path=args.profile_path, headless=args.headless) as browser:
        twitter = Twitter(browser)
        for url in urls:
            starttime = datetime.utcnow()
            logger.debug(f"!!! looking into {url}")
            browser.get(url)
            browser.wait(By.XPATH, ".//div[@data-testid='reply']")

            visited = {}
            tweeted = 0
            for tweet in twitter.get_tweets():
                for i in range(2):
                    if tweet.retweet_button is None or browser.is_element_visible_in_viewpoint(tweet.retweet_button): break
                    browser.page_down()

                key = tweet.url
                logger.debug(f"   --- checking visited {key}")
                if key not in visited:
                    visited[key] = True

                    # retweet those with many likes within certain period
                    if not tweet.liked and tweet.likes > args.min_likes and (datetime.utcnow() - tweet.time).total_seconds() / 60 / 60 < args.max_hours:
                        twitter.like_and_retweet(tweet)
                        tweeted += 1

                logger.debug(f"   visited:{len(visited)} tweeted:{tweeted} runtime:{str((datetime.utcnow() - starttime).total_seconds() / 60)}")
                
                if len(visited) > args.posts_to_read or tweeted >= args.posts_to_retweet or (datetime.utcnow() - starttime).total_seconds() / 60 >= args.max_run_minutes: break
                time.sleep(2)

            logger.debug(f"{url} visited {len(visited)} tweeted {tweeted}")

    logger.info("Bye\n")