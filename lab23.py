import re

def pan(pan_number):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, pan_number))
def email(email_id):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email_id))
PAN = input("Enter PAN number: ")
EMAIL = input("Enter Email ID: ")
if pan(PAN):
    print("PAN is Valid")
else:
    print("PAN is Invalid")

if email(EMAIL):
    print("Email is Valid")
else:
    print("Email is Invalid")
