# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

#filename == the recipient group file
#Format: name emailaddr
#        name emailaddr
#        name emailaddr
#        name emailaddr ... 
filename = ""
with open(filename, "r") as f :
    Group = f.read().split('\n')
    f.close()
print(Group)

# me == the sender's email address
# pwd = sender's email account password
me = ""
pwd = ""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(me, pwd)

for recipient in Group :
    if recipient == '' :
        continue
    name_and_addr = recipient.split()
    # Open the plain text file whose name is in textfile for reading.
    content = name_and_addr[0] + "教授您好\n        你他媽給我參加送舊賽喔幹"
    msg = EmailMessage()
    msg.set_content(content)

    # sub == Subject
    # you == the recipient's email address
    sub = "台大電機系桌送舊賽"
    you = name_and_addr[1]
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server.
    server.send_message(msg)

server.quit()
