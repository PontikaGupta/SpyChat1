# Importing datetime library to show date and time of chat
from datetime import datetime

# Using Spy class to store values of Spy
class Spy:
  # Using constructor
  def __init__(self, name, age, rating,is_online):
    # Initializing the values
    self.name = name
    self.age = age
    self.rating = rating
    self.is_online = is_online
    self.chats = []
    self.current_status_message = None

# For existing user
spy = Spy('Mr. Pontika',21,5.5,True)

# Existing friends of spy
friend_one = Spy('Mr. Sachin Sak', 23, 8,True)
friend_two = Spy('Mr. Sekhar Sharma', 23, 6.5,True)
friend_three = Spy('Mr. Rahul Kumar', 22,7,True)
friend_four = Spy('Mr. Satbeer Choudhary',22,7,True)

# List for storing friends of spy
friends = [friend_one, friend_two, friend_three,friend_four]

# Using ChatMessage class to store messages
class ChatMessage:
  # Using constructor
  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()  # now() function displays current date and time
    self.sent_by_me = sent_by_me


