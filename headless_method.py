import getpass 
import smtplib
from email.message import EmailMessage


user = input('Enter User Name :')

try: 
    password = getpass.getpass() 
except Exception as error: 
    print('ERROR', error)

server = smtplib.SMTP("smtp.gmail.com",587)

#Next, log in to the server
# number of recipient 
n = int(input("Enter number of recipient : ")) 

# Below line read inputs from user using map() function 
to = list(map(str,input("\nEnter the recipient : ").strip().split()))[:n] 

#print("\nList is - ", a) 

sent_from = user


subject = input("Enter the Subject : ")

#reading content from the terminal
body = input("Enter the content : ")

#reading content from a text file
# with open(textfile) as f:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(f.read())


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to).encode('utf-8'), subject.encode('utf-8'), body.encode('utf-8'))



server.ehlo()
server.starttls()
server.ehlo()
server.login(user, password)
server.sendmail(sent_from,to,email_text)

print('Email Sent!')
server.close()