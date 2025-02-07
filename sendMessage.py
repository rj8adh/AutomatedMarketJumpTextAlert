import smtplib
import sys
import os
 
CARRIERS = {
    "sprint": "@messaging.sprintpcs.com",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "att": "@mms.att.net"
}
 
EMAIL = ""
PASSWORD = ""
 
def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)

phoneNum = input("Enter Phone Number: ")
carrier = input("Enter Mobile Provider: ")
message = input("Send Message: ")

send_message(phoneNum, carrier, message)