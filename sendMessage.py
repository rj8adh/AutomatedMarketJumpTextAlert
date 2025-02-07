from dotenv import load_dotenv
import smtplib
import sys # In case we want delay later
import os

load_dotenv()

# print(EMAIL)
# print(PASSWORD)

def sendTextMessage(phone_number, carrier, message):

    # Common Mobile Phone Carriers and Corresponding Emails
    CARRIERS = {
    "sprint": "@messaging.sprintpcs.com",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "att": "@mms.att.net"
    }
 
    EMAIL = os.getenv("EMAIL_ADDRESS")
    PASSWORD = os.getenv("AUTH_KEY")

    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587) # 587 specifies that I'm using gmail

    # Logging in and authenticating my email
    server.starttls()
    server.login(auth[0], auth[1])
 
    # Actually sending the message
    server.sendmail(auth[0], recipient, message)

# The following code is in case you want to test the function by itself:

# phoneNum = input("Enter Phone Number: ")
# carrier = input("Enter Mobile Provider: ")
# message = input("Send Message: ")

# send_message(phoneNum, carrier, message)