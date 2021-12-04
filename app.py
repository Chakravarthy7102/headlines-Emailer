# for sending the network requests
import requests
# for webscrapping
from bs4 import BeautifulSoup

# send emails with smtp.lib
# starts the smtp server that sends emails to targetted emails.
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
    # interating through the soup according the websites structure and returns a html object as a result
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+"::"+tag.text+"\n"+"<br/>")
                if tag.text != 'More' else '')

    return cnt


url = "https://news.ycombinator.com/"

cntGlobal = extract_news(url)
content += cntGlobal
content += '<br>---------------<br>'
content += '<br><br>End Of The Email!'

# lets send the email

print('Composing Email...')

# update your email details

SERVER = 'smtp.gmail.com'  # "your smtp server"
PORT = 587  # your port number
FROM = ''  # "your from email id"
TO = ''  # "your to email ids"  # can be a list
PASS = ''  # "your email id's password"


print('Creating the email body')

msg = MIMEMultipart()

# message header / title

msg['Subject'] = 'Top news Headlines [Auto generated Email---Dont Reply]' + ' ' + \
    str(currentDate.day) + "-" + \
    str(currentDate.month)+'-'+str(currentDate.year)
msg['to'] = TO
msg['from'] = FROM

# attaching the webscrapped data to the email
msg.attach(MIMEText(content, 'html'))

# starting the server to send the mail to the targeted email
# a to emails can be bunch
# server =
