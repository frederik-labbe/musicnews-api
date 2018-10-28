# Music news API

## Retrieve new albums by category.

### Installation
- Install Python 3.6
- Get the package bs4 (Beautiful Soup)

### Usage

#### As a python module
``` python
from musicnews_api import MusicNewsAPI as API

if __name__ == '__main__':
    api = API('music_url') # replace music_url with preferred website

    results = api.get_albums('metal', sorted_by='style')
    
    print(
        '\n'.join([
            f"{x['artist']} - {x['album']}"
            for x in results
        ])
    )
```

#### As a command
<pre>
usage: main.py [-h] (--category CATEGORY | --view-categories) [--json]
               [--page PAGE] [--sort SORTED_BY] [--artist FILTER_ARTIST]
               [--album FILTER_ALBUM] [--released FILTER_RELEASED]
               [--style FILTER_STYLE] [--format FILTER_FORMAT]
               [--size FILTER_SIZE]

Retrieve new albums.

optional arguments:
  -h, --help            show this help message and exit
  --category CATEGORY, -c CATEGORY
                        The music category.
  --view-categories, -v
                        View categories.
  --json, -j            Outputs in JSON format.
  --page PAGE, -p PAGE  The result page.
  --sort SORTED_BY, -s SORTED_BY
                        Sort criteria.
  --artist FILTER_ARTIST, -a FILTER_ARTIST
                        The artist filter expression.
  --album FILTER_ALBUM, -b FILTER_ALBUM
                        The album filter expression.
  --released FILTER_RELEASED, -r FILTER_RELEASED
                        The released filter expression.
  --style FILTER_STYLE, -t FILTER_STYLE
                        The style filter expression.
  --format FILTER_FORMAT, -f FILTER_FORMAT
                        The format filter expression.
  --size FILTER_SIZE, -z FILTER_SIZE
                        The size filter expression.

</pre>
