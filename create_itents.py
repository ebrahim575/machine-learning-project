import json

f = open('chat.json',encoding="utf-8")
data = json.load(f)

intents_dict = {}
lst = []
lst2 = []
flag = 0
flag2 = 0


for i in range(len(data)):
    if data[i]['is_from_me'] == '0':  # all questions to me
        if flag == 1 and flag2 == 1:
            intents_dict['convoNum'] = str(i)
            intents_dict['patterns'] = lst
            intents_dict['responses'] = lst2
            with open('intents.json', 'a', encoding='utf-8') as f:
                json.dump(intents_dict, f, ensure_ascii=False, indent=4)
                f.write(',\n')
            flag = 0
            flag2 = 0
            flag3 = 0
            lst = []
            lst2 = []
            intents_dict = {}
        lst.append(data[i]['text'])
        flag = 1

    if data[i]['is_from_me'] == '1':  # all my responses
        lst2.append(data[i]['text'])
        flag2 = 1

