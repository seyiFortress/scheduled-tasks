# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random as rd
import smtplib as sm
from email.message import EmailMessage
import os

# import os and use it to get the Github repository secrets
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
date_time = dt.datetime.now()
present_date = str(date_time.date())


data = pd.read_csv("./birthdays.csv")
data["date"] = (data["year"].astype(str).str.cat(data["month"].astype(str), sep="-")).str.cat(data["day"].astype(str), sep="-")
dict_data = data.to_dict(orient="records")

# print(data.name)
for (index, row) in data.iterrows():
    if row.date == present_date:


        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letters: list = []
        with open("./letter_templates/letter_1.txt") as letter_1:
            content_list = letter_1.readlines()
            letters.append(content_list)
        with open("./letter_templates/letter_2.txt") as letter_2:
            content_list = letter_2.readlines()
            letters.append(content_list)
        with open("./letter_templates/letter_3.txt") as letter_3:
            content_list = letter_3.readlines()
            letters.append(content_list)

        rand_letter = rd.choice(letters)
        # print(rand_letter)

        rand_letter = rand_letter.replace("[NAME]", row.name)

        # 4. Send the letter generated in step 3 to that person's email address.
        msg = EmailMessage()
        msg["Subject"] = f"Happy Birthday {row.name}"
        msg["From"] = my_email
        msg["To"] = row.email
        msg.set_content(rand_letter)

        connection = sm.SMTP("smtp.aol.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.send_message(msg)
        connection.close()
