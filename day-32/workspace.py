# import smtplib

# my_email="rithishtest@gmail.com"
# password="ex2e2s"

# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="rithishtestemail@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of the email")
# import datetime as dt

# now=dt.datetime.now()
# date=now.weekday()
# month=now.month
# date_of_birth=dt.datetime(year=2000,month=12,day=13,hour=3,minute=33)
# print(date_of_birth)
import smtplib
import datetime as dt
import random

list=[]
my_email="rithishtest@gmail.com"
password="edgo wxmh azvg xdtm"
now=dt.datetime.now()

today=now.weekday()

with open("quotes.txt") as quotes:
    list=quotes.readlines()
    random_quote=random.choice(list)

if today==0:
    print(today)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="rithishtestemail@yahoo.com",
                        msg=f"Subject:Quote of Monday\n\n{random_quote}")
