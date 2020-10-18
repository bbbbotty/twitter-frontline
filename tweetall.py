from ff import init as browser_init
import argparse
import re
import time
from datetime import datetime
import logging
import utils
import os

if __name__ == "__main__":

    config = utils.read_config()

    parser = argparse.ArgumentParser(description='Retweet all tweets in a file')
    parser.add_argument('url_or_file', nargs='?', default=config.tweetall.url_or_file)
    parser.add_argument('--delete_file', action='store_true', default=config.tweetall.delete_file)
    parser.add_argument('--executable_path', default=config.executable_path)
    parser.add_argument('--profile_path', default=config.profile_path)
    parser.add_argument('--headless', action='store_true', default=config.headless)
    parser.add_argument('--history', default=config.tweetall.history)
    parser.add_argument('--debug', action='store_true', default=config.debug)

    args = parser.parse_args()

    logger = utils.get_logger(logging.INFO if not args.debug else logging.DEBUG)

    logger.info('start')

    regex = re.compile(r"https://(?:www\.)?twitter\.com/.+\/status\/[^\s]+")
    urls = set()
    with browser_init(executable_path=args.executable_path, profile_path=args.profile_path, headless=args.headless) as browser:
        if os.path.exists(args.url_or_file):
            with open(args.url_or_file, newline="", encoding="utf-8") as f:
                for line in f:
                    for url in regex.findall(line):
                        urls.add(url)
        else:
            browser.get(args.url_or_file)
            time.sleep(5)
            for a in browser.find_elements_by_tag_name('a'):
                for url in regex.findall(a.get_attribute('href')):
                    urls.add(url)

        utils.retweet_all(browser, urls, args.history)

    if os.path.exists(args.url_or_file) and args.delete_file:
        os.remove(args.url_or_file)
        logger.info(f"{args.url_or_file} removed")

    logger.info('Bye\n')
