import os
import smtplib

class NotificationManager:
    def send_email(self,to_email,subject,body):
        with smtplib.SMTP("smtp.gmail.com",587)as connection:
            connection.starttls()
            connection.login(
                user=os.environ["MY_EMAIL"],
                password=os.environ["MY_PASS"]
            ) 
            connection.sendmail(from_addr=os.environ["MY_EMAIL"],to_addrs=to_email,msg=f"Subject: {subject}\n\n{body}")
            
