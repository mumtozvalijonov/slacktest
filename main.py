import os
import slack
from config import TOKEN

client = slack.WebClient(token=TOKEN)

file_path = 'YOUR FILE PATH'
client.users_setPhoto(image=file_path)
