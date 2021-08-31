import json
import csv

def get_messages():
    f = open('chat.json',encoding="utf-8")
    data = json.load(f)
    f2 = open("my_messages.txt", "w")
    f3 = open("nation_messages.txt", "w")
    for i in range(len(data)):
        try:
            if data[i]['is_from_me'] == '1':
                tempStr = data[i]['text'].replace("’","")
                tempStr = tempStr.replace("“","")
                tempStr = tempStr.replace("”","")
                f2.write(tempStr + '\n')
            if data[i]['is_from_me'] == '0':
                tempStr = data[i]['text'].replace("’", "")
                tempStr = tempStr.replace("“", "")
                tempStr = tempStr.replace("”", "")
                f3.write(tempStr + '\n')
        except:
            continue
    f2.close()
    f3.close()

get_messages()