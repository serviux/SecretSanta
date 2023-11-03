import pandas as pd
import random
import logging
from send_email import EmailSender
from Person import Person

format = "[%(levelname)s]: %(message)s"
logging.basicConfig(filename='santa.log',
                    filemode='w',
                    level=logging.INFO,
                    format=format)


def main():
  df = pd.read_csv("particpants.csv", header=0)

  participant_list = []
  for _, row in df.iterrows():
    temp = Person(None, None, None, None)
    temp.name = row["Name"]
    temp.email = row["Email"]
    participant_list.append(temp)

  random.shuffle(participant_list)
  for i in range(len(participant_list)):
    if i + 1 < len(participant_list):
      p1 = participant_list[i]
      p2 = participant_list[i + 1]
      p1.secret_santa_email = p2.email
      p1.secret_santa_name = p2.name
      participant_list[i] = p1
    else:
      p1 = participant_list[i]
      p2 = participant_list[0]
      p1.secret_santa_email = p2.email
      p1.secret_santa_name = p2.name
      participant_list[i] = p1

  logging.info(participant_list)
  # change this to false to send the secret santa message
  send_alert = False

  email_sender = EmailSender()
  for person in participant_list:
    email_sender.send_email(person, alert_user=send_alert)


if (__name__ == "__main__"):
  main()
