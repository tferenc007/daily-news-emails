import requests
from send_email import send_email
api_key ='ebb30b1152ac42998a5a222ab3cb2801'

url ='http://newsapi.org/v2/everything?q=tesla&from=2024-03-12&' \
    'sortBy=publishedAt&apiKey=ebb30b1152ac42998a5a222ab3cb2801'
# url = 'http://onet.pl'

request = requests.get(url)

content = request.json()

body = ''
for article in content["articles"]:
    if article["title"] is not None:
        body = body + str(article["title"]) + '\n' + str(article["description"]) + 2*'\n'

body = body.encode("utf-8")
send_email(message=body)