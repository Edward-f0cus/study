#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pudb import set_trace
set_trace()

import requests
import os
import shutil
import logging
import sys
import time
import argparse
from bs4 import BeautifulSoup
from datetime import date, timedelta

URL = 'http://x77913.net/bbs/thread.php?fid=18'
URL_BASE = 'http://x77913.net/bbs/'
FAIL_FLAG = 0
PWD = os.getcwd()
HTMLS_DIR = os.path.join(PWD, 'htmls')
PICS_DIR = os.path.join(PWD, 'pics')

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--single', help='url of single mode')
parser.add_argument('-t', '--timeout', help='timeout of delay',
                    default=30, type=int)
args = parser.parse_args()
timeout = args.timeout


def sleep_wrapper(timeout=timeout):
    def outter(func):
        def inner(*args, **kwargs):
            logging.info('wait %s seconds...' % timeout)
            time.sleep(timeout)
            func(*args, **kwargs)
        return inner
    return outter


def get_today():
    today = date.today()
    return today.isoformat()


def get_yesterday():
    yesterday = date.today() - timedelta(1)
    return yesterday.isoformat()


def encode_url(url):
    url = url.replace('?', '\?')
    url = url.replace('=', '\=')
    return url


def get_homepage():
    os.chdir(HTMLS_DIR)
    r = requests.get(URL, timeout=90)
    with open('homepage.html', 'w') as f:
        f.writelines(r)
    with open('homepage.html') as f1:
        lines = f1.readlines()
        if len(lines) < 2:
            logging.critical('No content in homepage')
            logging.debug(lines[0])
            sys.exit(1)
    os.chdir(PWD)


def get_aims():
    os.chdir(HTMLS_DIR)
    href_cont = {}
    aim_dates = []
    soup = BeautifulSoup(open('homepage.html'))
    div_tag = soup.find_all('div', class_='z threadCommon')[0]
    tr3_tags = div_tag.find_all('tr', 'tr3')
    for tr3_tag in tr3_tags:
        aim_href = tr3_tag.find(class_='subject').find('a').get('href')
        aim_cont = tr3_tag.find(class_='subject').find('a').string
        aim_date = tr3_tag.find(class_='author').find('p').string
        aim_dates.append(aim_date)
        aim_url = URL_BASE + aim_href
        today = get_today()
        # If today has no posts, then process yesterday's posts
        if aim_date == today or aim_date == get_yesterday() and \
                today not in aim_dates:
            href_cont[aim_url] = aim_cont
    os.chdir(PWD)
    return href_cont


@sleep_wrapper(timeout=timeout)
def get_aim_html(url, filename):
    os.chdir(HTMLS_DIR)
    try:
        r_aim = requests.get(url, timeout=90)
        with open(filename, 'w') as f:
            f.writelines(r_aim)
    except:
        logging.error('Timed out to access aim html')
    os.chdir(PWD)


def download_pic(addr, filename):
    logging.debug('address and filename: %s, %s' % (addr, filename))
    try:
        r = requests.get(addr, timeout=20)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
    except:
        logging.error('Timed out to download pic')


def clean_pics():
    if os.path.exists(HTMLS_DIR):
        shutil.rmtree(HTMLS_DIR)
    if os.path.exists(PICS_DIR):
        shutil.rmtree(PICS_DIR)
    os.mkdir(PICS_DIR)
    os.mkdir(HTMLS_DIR)


def doesNeedRerun(html):
    os.chdir(HTMLS_DIR)
    with open(html) as f:
        if len(f.readlines()) < 3:
            logging.info('No content found in %s, need to rerun!' % html)
            os.chdir(PWD)
            return True
        else:
            os.chdir(PWD)
            return False


def process_aim(filename, foldername):
    os.chdir(HTMLS_DIR)
    aim_soup = BeautifulSoup(open(filename))
    aim_div_tags = aim_soup.find_all('div', id='read_tpc')
    if not aim_div_tags:
        logging.error('No content found in %s' % filename)
        # if html has no content, then skip it and continue
        return
    aim_div_tag = aim_div_tags[0]
    aim_img_tags = aim_div_tag.find_all('img')
    pic_names = [str(x) for x in range(len(aim_img_tags))]
    logging.debug('pic names in process_aim is %s' % pic_names)

    os.chdir(PICS_DIR)
    os.mkdir(foldername)
    os.chdir(foldername)
    logging.debug('cur dir is %s' % os.getcwd())

    for name, tag in zip(pic_names, aim_img_tags):
        tag_src = tag.get('src')
        postfix = '.' + str(tag_src).split('.')[-1]
        logging.debug('post fix is: %s' % postfix)
        name = name + postfix
        logging.debug('file name in %s is: %s' % (foldername, name))
        aim_pic_addr = tag.get('src')
        logging.debug('address of %s is: %s' % (name, aim_pic_addr))
        download_pic(aim_pic_addr, name)
    os.chdir(PWD)


def main():
    clean_pics()

    get_homepage()

    aim_dict = get_aims()
    html_names = [str(x) + '.html' for x in range(len(aim_dict))]
    for aim_url, html_name in zip(aim_dict.keys(), html_names):
        logging.debug('url and html name: %s, %s' % (aim_url, html_name))
        get_aim_html(aim_url, html_name)
        rerun_flag = doesNeedRerun(html_name)
        rerun_time = 3

        for i in range(rerun_time):
            if rerun_flag:
                get_aim_html(aim_url, html_name)
                rerun_flag = doesNeedRerun(html_name)
            else:
                break

        foldername = aim_dict[aim_url]
        try:
            process_aim(html_name, foldername)
        except:
            logging.error('process %s failed' % aim_url)


def jerk_with_single(url):
    clean_pics()

    get_aim_html(url, 'single.html')
    process_aim('single.html', 'single')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(funcName)s] -- %(lineno)s: %(message)s')

    if not args.single:
        main()
    else:
        jerk_with_single(parser.single)
