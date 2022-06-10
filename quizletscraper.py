from bs4 import BeautifulSoup
import requests

url = "https://quizlet.com/330826762/what-is-a-url-flash-cards/"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"

headers = {"user-agent": USER_AGENT}

response = requests.get(url, headers=headers)

if response.status_code == 200 :
    document = BeautifulSoup(response.content, "html.parser")
    print(document.prettify())


