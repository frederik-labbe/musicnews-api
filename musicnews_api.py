import os
import re
import utils


class MusicNewsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_categories(self):
        main_url = self.base_url
        doc = utils.soup_parse_url(main_url)

        results = [
            {
                'name': cat.text.strip(),
                'href': cat.find('a').attrs['href']
            }
            for cat in doc.find_all('li', 'cat-item')
            if not cat.find('ul', 'children') and 'video' not in cat.text.lower()
        ]

        return results

    def get_albums(self, category, page=None, **kwargs):
        cat_url = os.path.join(self.base_url, 'category', category)
        if page is not None:
            cat_url = os.path.join(cat_url, 'page', str(page))

        doc = utils.soup_parse_url(cat_url)

        results = [
            {
                'artist': utils.subs_in_between(entry.text, 'Artist:', 'Album:').strip(),
                'album': utils.subs_in_between(entry.text, 'Album:', 'Released:').strip(),
                'cover': entry.find('img').attrs['src'],
                'released': utils.subs_in_between(entry.text, 'Released:', 'Style:').strip(),
                'style': utils.subs_in_between(entry.text, 'Style:', 'Format:').strip(),
                'format': utils.subs_in_between(entry.text, 'Format:', 'Size:').strip(),
                'size': utils.subs_in_between(entry.text, 'Size:', 'Mb').strip() + ' Mb',
                'href': entry.find('a').attrs['href']
            }
            for entry in doc.find_all('div', 'entry')
        ]

        if kwargs.get('sorted_by'):
            results = sorted(results, key=lambda x: x[kwargs['sorted_by']])

        if kwargs.get('filter_artist'):
            results = [x for x in results if re.match(kwargs['filter_artist'], x['artist'].lower())]

        if kwargs.get('filter_album'):
            results = [x for x in results if re.match(kwargs['filter_album'], x['album'].lower())]

        if kwargs.get('filter_released'):
            results = [x for x in results if re.match(kwargs['filter_released'], x['released'].lower())]

        if kwargs.get('filter_style'):
            results = [x for x in results if re.match(kwargs['filter_style'], x['style'].lower())]

        if kwargs.get('filter_format'):
            results = [x for x in results if re.match(kwargs['filter_format'], x['format'].lower())]

        if kwargs.get('filter_size'):
            results = [x for x in results if re.match(kwargs['filter_size'], x['size'].lower())]

        return results
