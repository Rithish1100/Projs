##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
import os

my_email=os.environ.get("MY_EMAIL")
password=os.environ.get("MY_PASSWORD")
today=dt.datetime.now()
today_tuple=(today.month,today.day)
data=pd.read_csv('day-32/birthdays.csv')
birthday_dict={(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple] 
    random_num=random.randint(1,3)
    with open(f"day-32/letter_templates/letter_{random_num}.txt") as letters:
        ran_letter=letters.read()
        ran_letter=ran_letter.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587)as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="rithishtestemail@yahoo.com",
                            msg=f"Subject:Happy Birthday!\n\n{ran_letter}")
print(today_tuple)
print(birthday_dict.keys())
    




