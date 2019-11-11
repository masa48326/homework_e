import time

import requests

response = requests.get(f'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

informations = response.json()

for i in range(0, 5):
    response_top5 = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{informations[i]}.json?print=pretty')
    time.sleep(1)
    information_top5 = response_top5.json()

    print("{'title': " + information_top5['title'] + ", 'link': " + information_top5['url'] + "}")
