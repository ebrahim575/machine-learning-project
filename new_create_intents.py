import json

f = open('chat.json',encoding="utf-8")
data = json.load(f)
my_messages = []
nation_messages = []

answers = {}
questions = {}
info = {}
declaration = {}
greeting = {}
thanks = {}
goodbye = {}

for i in range(len(data)):
    if data[i]['is_from_me'] == '1':
        my_messages.append(data[i]['text'])
    if data[i]['is_from_me'] == '0':
        nation_messages.append(data[i]['text'])

