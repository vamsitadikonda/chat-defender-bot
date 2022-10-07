## Work Flow
Whenever a new message is posted on Discord, the Chat Defender Bot implements the Profanity checker and the Bully checker on the text of the message. 
The profanity checker verifies each part of the text against the words classified as profanity in the database, while the bully checker runs a machine 
learning model to check if the message is toxic in nature. If it passes both the checks without encountering an offense, the model further checks if the 
user is apologising for a previous offense, and updates their data in the database accordingly. In case the user is reporting a word as profanity, the bot 
updates the word list. However, if an offence is detected, the users' offense count is updated, and a warning message is sent out if it is a first offense.
If not, the user will be banned, and notified of the same.
![image](https://drive.google.com/uc?export=view&id=1bWt3snkgL4JocSx6DPmJqnlSlbxDd3qE)
