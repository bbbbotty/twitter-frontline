from ff import init as browser_init
import argparse
import re
import time
from datetime import datetime
import utils
import os

parser = argparse.ArgumentParser(description='Retweet all tweets in a file')
parser.add_argument('url_or_file', nargs='?', default='tweet_list.txt')
parser.add_argument('--headless', action='store_true', default=False)
parser.add_argument('--executable_path', default=r"ff\App\Firefox64\firefox.exe")
parser.add_argument('--profile_path', default=r"ff\Data\profile")

args = parser.parse_args()

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

    utils.retweet_all(browser, urls)

print("bye " + str(datetime.now()))
print("")

quit()
