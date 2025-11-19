import requests
from requests.models import StreamConsumedError
from requests.exceptions import Timeout

teleURL = 'http://192.168.8.113:1444/api/transformer/sendNotificationToTelegramGroup'

messages = "Test"
pload = {'message':messages}

print("Sending message : " + messages)
r = requests.post(teleURL, data = pload, timeout = 5, verify = False)
print(r)