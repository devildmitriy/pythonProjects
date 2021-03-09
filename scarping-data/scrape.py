import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.title>.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnList):
    return sorted(hnList, key=lambda post: post['votes'], reverse=True)


def create_custom_hn(posts, votes):
    hn = []

    for idx, item in enumerate(posts):
        vote = votes[idx].select('.score')
        if len(vote):
            title = posts[idx].getText()
            href = posts[idx].get('href', None)
            point = int(vote[0].getText().split(' ')[0])
            if point > 500:
                hn.append({'title': title, 'link': href, 'votes': point})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
