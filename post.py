#!/usr/bin/env python3.6

# the messager5000 allows users to send messages to new or exisitng conversations without the hassle of typing out those curl commands.

import os
import requests
import json

#prompt user for message information
sender = input("Who is sending this message? ")
conversation_id = input("Which conversation would you like to send it to?(id) ")
message = input("Please type your message... ")

#send the message

payload = {'sender': sender, 'conversation_id': conversation_id, 'message': message}
url = 'http://localhost:5000/convoDB/conversations'

req = requests.post(url, json=payload)


print(f"Your message has been sent, thanks {sender}!")
print()
