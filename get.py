#!/usr/bin/env python3.6

# the get allows users to retieve conversations without the need of curl commands

import os
import requests
import json

#prompt user for conversation id
conversation_id = input("Which conversation would you like to see?(id) ")

#get the conversation
print()
os.system(f"curl -i http://localhost:5000/convoDB/conversations/{conversation_id}")

print()
print(f"End of conversation")
print()
