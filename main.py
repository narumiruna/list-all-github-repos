import json

import click
import requests


def get_repos(access_token, per_page=100, max_pages=10):
    # https://developer.github.com/v3/repos/#list-your-repositories
    url = 'https://api.github.com/user/repos'

    page = 0
    with requests.session() as sess:
        for page in range(1, max_pages + 1):
            payload = dict(access_token=access_token,
                           per_page=per_page,
                           page=page)

            res = sess.get(url, params=payload)
            repos = json.loads(res.text)

            if not repos:
                return

            for repo in repos:
                yield repo


@click.command()
@click.option('-a', '--access-token')
def main(access_token):
    repos = get_repos(access_token)

    for repo in repos:
        print(repo['ssh_url'])


if __name__ == '__main__':
    main()
