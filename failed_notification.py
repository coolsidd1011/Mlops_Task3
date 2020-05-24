#!/usr/bin/env python
# coding: utf-8

# In[4]:


import smtplib, ssl
import getpass
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "siddcool1011@gmail.com"
receiver_email = "coolsidd1997@gmail.com"
password =getpass.getpass('enter pass ->')
message = """Subject: Hi there

GOOD AFTERNOON SIR>................
THIS  mail is on bhealf of your model

...........................
Your model is  not trained as you wished it to be 

...........

Don't lose hope..try again....I wish you will get success in next try

.......Happy day sir.......enjoy!!!!!!!!!!!!!
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[ ]:




