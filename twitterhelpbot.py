import time
from datetime import datetime
import os
from twitter import Twitter
from ff import init as browser_init
import argparse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import urllib.parse
import logging
import utils

if __name__ == "__main__":

    config = utils.read_config()

    parser = argparse.ArgumentParser(description='Retweet links in twitter helper bot')
    parser.add_argument('--wait', default=config.twitterhelpbot.wait, type=int)
    parser.add_argument('--continuation', action='store_true', default=False)
    parser.add_argument('--executable_path', default=config.executable_path)
    parser.add_argument('--profile_path', default=config.profile_path)
    parser.add_argument('--headless', action='store_true', default=config.headless)
    parser.add_argument('--history', default=config.twitterhelpbot.history)
    parser.add_argument('--output_file', default=config.twitterhelpbot.output_file)
    parser.add_argument('--debug', action='store_true', default=config.debug)

    args = parser.parse_args()

    logger = utils.get_logger(logging.INFO if not args.debug else logging.DEBUG)

    logger.info("start")

    commands = ["香港直擊", "國際戰線", "外語新聞"]
    with browser_init("https://web.telegram.org/#/im?p=@TwitterHelpBot", executable_path=args.executable_path, profile_path=args.profile_path, headless=args.headless) as browser:
        browser.wait(By.CLASS_NAME, "im_dialog", args.wait)
        time.sleep(5)
        input = browser.find_element_by_class_name("composer_rich_textarea")
        urls = []

        if args.continuation:
            for url in [a.get_attribute('href') for a in browser.find_elements_by_xpath("(//div[@class='im_message_text'])[last()]/a")[:-1]]: 
                urls.append(urllib.parse.unquote(re.search('url=(.+)', url).group(1)))
        else:
            for command in commands:
                logger.info(command)

                input.send_keys("/task")
                input.send_keys(Keys.ENTER)
                time.sleep(2)
                browser.find_elements_by_xpath(f"//button[text()='{command}...']")[-1].click()
                time.sleep(5)

                for url in [a.get_attribute('href') for a in browser.find_elements_by_xpath("(//div[@class='im_message_text'])[last()]/a")[:-1]]: 
                    urls.append(urllib.parse.unquote(re.search('url=(.+)', url).group(1)))
        
        if args.output_file is not None and len(args.output_file) > 0:
            utils.save_all(urls, args.output_file)
        else:
            logger.info("Retweet all now")
            utils.retweet_all(browser, urls, args.history)

    logger.info('Bye\n')
