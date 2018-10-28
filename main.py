#!/usr/bin/env python3
import argparse
import json
from musicnews_api import MusicNewsAPI


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve new albums.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--category', '-c', dest='category', type=str, help='The music category.')
    group.add_argument('--view-categories', '-v', dest='view_categories', help='View categories.', action='store_true')
    parser.add_argument('--json', '-j', dest="json_format", help='Outputs in JSON format.', action='store_true')
    parser.add_argument('--page', '-p', dest='page', type=str, help='The result page.')
    parser.add_argument('--sort', '-s', dest='sorted_by', type=str, help='Sort criteria.')
    parser.add_argument('--artist', '-a', dest='filter_artist', type=str, help='The artist filter expression.')
    parser.add_argument('--album', '-b', dest='filter_album', type=str, help='The album filter expression.')
    parser.add_argument('--released', '-r', dest='filter_released', type=str, help='The released filter expression.')
    parser.add_argument('--style', '-t', dest='filter_style', type=str, help='The style filter expression.')
    parser.add_argument('--format', '-f', dest='filter_format', type=str, help='The format filter expression.')
    parser.add_argument('--size', '-z', dest='filter_size', type=str, help='The size filter expression.')
    args = parser.parse_args()

    api = MusicNewsAPI('music_url') # replace music_url with preferred website

    if args.view_categories:
        results = api.get_categories()

        print(
            json.dumps(results)
            if args.json_format
            else (
                '\n'.join([
                    f"{r['name']}\n" +
                    f"[{r['href']}]\n"
                    for r in results
                ]).strip()
            )
        )
    else:
        results = api.get_albums(
            args.category,
            page=args.page,
            sorted_by=args.sorted_by,
            filter_artist=args.filter_artist,
            filter_album=args.filter_album,
            filter_released=args.filter_released,
            filter_style=args.filter_style,
            filter_format=args.filter_format,
            filter_size=args.filter_size
        )

        print(
            json.dumps(results)
            if args.json_format
            else (
                '\n'.join([
                    f"{r['artist']} - {r['album']} ({r['style']}) @ {r['format']} ({r['size']})\n" +
                    f"[{r['href']}]\n"
                    for r in results
                ]).strip()
            )
        )
