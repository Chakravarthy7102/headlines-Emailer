# for sending the network requests
import requests
# for webscrapping
from bs4 import BeautifulSoup
# send emails with smtp.lib
import smtplib
# for the emails body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# for playing arround with the system date and time
import datetime

# current date and time

currentDate = datetime.datetime.now()

# a empty email placeHolder
content = ''


# extracting the headline stories


def extract_news(url):

    cnt = ''
    response = requests.get(url)
    innerContent = response.content
    soup = BeautifulSoup(innerContent, 'html.parser')

    print(soup)
    # interating through the soup according the websites structure and returns a html object as a result
    # for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
    #     print(i, tag)


url = "https://news.ycombinator.com/"

extract_news(url)
