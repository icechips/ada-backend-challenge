This is the instructions for using the Messager5000

I gave this assessment my best shot. I've never done something like this so everything youll see I had to basicsally learn on the spot. I know its not perfect, but I spent some good hours on it and I look forward to the feedback.

Their are two requierments that must be installed in order for this app to run. The Flask and Requests python libs.

To install them:

	pip install flask
	pip install requests


There are four files that are used for the app

get.py  messager5000.py  post.py  webapp.py

webapp.py
	- this script hosts the flask webserver, and handles the dict data posting and getting

post.py
	- this script is called by the messager5000 to handle the http post requests

get.py
	- this script is also called by the messager5000 to handle the http get requests

messager5000.py
	- this is the main application script. The end user can start up this script and do everything from here. The options are presented in a straight-forward menu with three options
		1. Send message
            	2. View conversation history
            	3. Quit
	
	1. Send Message

		- using the post.py script, this allows the end user to send a message to the conversation of their choice by specifying the conversation id

	2. View Conversation History

		- using the get.py script, this allows the end user to view all messages of a conversation by specifying the conversation id.

	3. Quit

		- exits the application


Conversation Persistance

	- i didnt manage to get that working 100%, but i did spend alot of time trying to. I got very close, but now im stuck. Theres a comment in the webapp.py script that explains why.
