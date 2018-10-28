import requests
from random import random
from bs4 import BeautifulSoup


def http_get(url, max_retry=5, retry_count=0, **kwargs):
    # Chrome Windows (actually not)
    chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

    # A weird but potential email
    email_from = f"user{random() * 1e6}@usherbrooke.ca"

    headers = {
        'User-Agent': chrome_ua,
        'From': email_from,
        'Accept-Encoding': 'gzip, deflate, br'
    }

    response = requests.get(url, headers)

    if response.status_code != 200:
        debug_print('Warning: The url {} responded with status {}'.format(url, response.status_code), **kwargs)
        return None

    content = response.content.decode(kwargs['encoding']) if kwargs.get('encoding') else response.content

    if kwargs.get('must_be_there'):
        if kwargs['must_be_there'] not in str(content):
            if retry_count < max_retry:
                debug_print('Warning: "must_be_there" was not returned by {}'.format(url), **kwargs)
                return http_get(url, retry_count + 1, **kwargs)
            else:
                debug_print(''.join([
                    'Warning: the "must_be_there" could not be found in the content for {} times in a row',
                    'None will be returned']
                ), **kwargs)
                return None

    debug_print('GET {} was successful after {} retry'.format(url, retry_count), **kwargs)
    return content


def soup_parse_url(url, **kwargs):
    page_content = http_get(url, **kwargs)
    return BeautifulSoup(page_content, 'html.parser') or None


def debug_print(msg, **kwargs):
    if kwargs.get('debug'):
        print('[DEBUG] {}'.format(msg))


def info_print(msg, **kwargs):
    if kwargs.get('info'):
        print('[INFO] {}'.format(msg))


def subs_in_between(expr, part_a, part_b):
    return expr.split(part_a)[1].split(part_b)[0]
