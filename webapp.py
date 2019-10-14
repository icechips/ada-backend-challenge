#!/usr/bin/env python3.6

# an http web conversation app that can write messages to conversations and view conversations


from flask import Flask
from flask import jsonify
from flask import request
import datetime
import json

#creates a flask app object
app = Flask(__name__)


#createing a dictionary  for conversations

convoDB=[
        {
            "conversation_id": "0001",
            "messages": [
                {
                    "sender": "joe",
                    "message": "the best hockey team is?",
                    "created": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                },
                {
                    "sender": "naomi",
                    "message": "toronto maple leafs!",
                    "created": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                }
            ]
        },
        {
            "conversation_id": "0002",
            "messages": [
                {
                    "sender": "joe",
                    "message": "the worst hockey team is?",
                    "created": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                },
                {
                    "sender": "naomi",
                    "message": "montreal canadiens!",
                    "created": '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                }
            ]
        }
    ]


#GET all convos
#@app.route('/convoDB/conversations',methods=['GET'])
#def getALLConvo():

    #load from json file for persistance
#    with open('convoDB.json', 'r') as f:
#        convoDB = json.load(f)

#    return jsonify({'convos':convoDB})


#GET a specific convo
@app.route('/convoDB/conversations/<convoID>', methods=['GET'])
def getConvo(convoID):

    #load from json file for persistance
    with open('convoDB.json') as f:
        convoDB = json.load(f)

    usr = [ convo for convo in convoDB if (convo['conversation_id'] == convoID) ]

    return jsonify({'convo':usr})



#POST new messages
@app.route('/convoDB/conversations', methods=['POST'])
def createMsg():
    msg = {
            'sender':request.json['sender'],
            'conversation_id':request.json['conversation_id'],
            'message':request.json['message'],
            'created': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) 
            }
    convoDB.append(msg)

    #save to json file for persistance
    with open('convoDB.json', 'w') as f:
        json.dump(convoDB, f)

    #that was with open('convoDB.json', 'a') as f
    #which did append the messages correctly, the only problem was, it would break the loading of the 
    #json file in the getConvo function. I had trouble finding a way to solve that issue.

    return jsonify(msg)

    



# run the app
@app.route("/")

def hello():
    return "Welcome to the Messager5000"
    
if __name__ == "__main__":
        app.run()



