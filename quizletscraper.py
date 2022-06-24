from bs4 import BeautifulSoup
import requests

url = "https://quizlet.com/479658931/chapter-17-preoperative-nursing-management-flash-cards/?i=2wz98s&x=1jqY"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
headers = {"user-agent": USER_AGENT}

response = requests.get(url, headers=headers)

# On request successful (200), 
if response.status_code == 200 :
    document = BeautifulSoup(response.content, "html.parser")
    for i, (question, answer) in enumerate(zip(document.select('a.SetPageTerm-wordText'), document.select('a.SetPageTerm-definitionText')), 1):
        print('QUESTION {}:'.format(i))
        print()
        print(question.get_text(strip=True, separator='\n'))
        print()
        print(answer.get_text(strip=True, separator='\n'))
        print('\n\n')
