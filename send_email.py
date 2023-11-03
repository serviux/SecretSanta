import ssl
import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Person import Person


class EmailSender():

  def __init__(self):
    self.sender = os.environ['email']
    self.password = os.environ['password']
    self.subject = "Secret Santa USE THIS ONE"

  def __make_html_message(self, person: Person):
    return f"""    <html>
<head>
<style>
        strong {{font-size: 200%;}}
</style>
</head>
<p>Greetings {person.name},<br></p>
<p>You have been enrolled in the Funny Men Secret Santa, my condolences. This year you have
        the pleasure of getting <strong>{person.secret_santa_name}</strong> a game. Please gift it to them on steam or send them a code
        at <strong>{person.secret_santa_email}</strong>.<br>. Please try to keep the value under $30 dollars, and send the gift by December 20th. \nHappy holidays</p>

<p>For your information the steam winter sale starts on the 21st of December</p>


<img width="480px" height="480px" src="https://media.giphy.com/media/9w475hDWEPVlu/giphy.gif">


</html>"""

  def send_email(self, person: Person, alert_user=False):

    message = MIMEMultipart()
    message["From"] = self.sender
    message["To"] = person.email
    message["Subject"] = self.subject
    body = ""
    html = ""
    if (not alert_user):
      html = self.__make_html_message(person)
    else:
      html = f"""
      <html>
        <p>Hello {person.name}</p>
        <p>This is a test to ensure that everyone is enrolled in the Funnymen secret Santa program. Here are some quotes from your fellow man</p>
        <p><q>Your Mom</q> <em>--Quotevante2022</em></p>
        <p><q>hohohoping to be urs winky emoji JK... Unless?</q> <em>--Patrick MacCarthey/Them</em></p>
</html>"""

    # message.attach(MIMEText(body, "plain"))
    message.attach(MIMEText(html, "html"))

    text = message.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(self.sender, self.password)
      server.sendmail(self.sender, person.email, text)
