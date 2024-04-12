import requests
from send_email import send_email
api_key ='ebb30b1152ac42998a5a222ab3cb2801'
topic = 'tesla'
url ='http://newsapi.org/v2/everything?' \
     f'q={topic}' \
     '&from=2024-03-12&' \
     'sortBy=publishedAt&' \
     f'apiKey={api_key}&' \
     'language=en'
# url = 'http://onet.pl'

request = requests.get(url)

content = request.json()

body = "Subject: Today's news" + '\n'
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + str(article["title"])  \
            + '\n' + str(article["description"]) \
            + '\n' + article["url"]+ 2*'\n'

body = body.encode("utf-8")
send_email(message=body)