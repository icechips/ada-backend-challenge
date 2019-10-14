#!/usr/bin/env python3.6

#the messager5000 allows users to send messages to differnet conversations, and to see conversation history.

import sys
import os

    
#make a menu
def menu():

    print("     **********Messager5000**********")
    print()

    choice = input("""
            1. Send message
            2. View conversation history
            3. Quit

            Please enter your selection: """)

    if choice == "1":
        print()
        print("Send Message")
        print()
        os.system('./post.py')

        menu()

    elif choice == "2":
        print()
        print("View Conversation History")
        print()
        os.system('./get.py')

        menu()

    elif choice == "3":
        print()
        print("Goodbye!")
        print()
        sys.exit

    else:
        print()
        print("Im sorry, thats not a valid option.")
        print()
        menu()


    

#draw the menu
menu()
