import json
import csv

f = open('chat.json', encoding="utf-8")
data = json.load(f)
intents_dict = {}



my_answer_lst = []
my_statement_lst = []
my_question_lst = []

nation_question_lst = []
nation_answer_lst = []
nation_statement_lst = []

with open('nation_messages_monkeylearn.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        if row[1] == 'question':
            nation_question_lst.append(row[0])
        if row[1] == 'answer':
            nation_answer_lst.append(row[0])
        if row[1] == 'statement':
            nation_statement_lst.append(row[0])


with open('my_messages_monkeylearn.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        if row[1] == 'answer':
            my_answer_lst.append(row[0])
        if row[1] == 'statement':
            my_statement_lst.append(row[0])
        if row[1] == 'question':
            my_question_lst.append(row[0])


#intents_dict['tag'] = 'answers'
# intents_dict['tag'] = 'question'
# intents_dict['tag'] = 'statement'

with open('intents2.json', 'a', encoding='utf-8') as f:
    intents_dict['tag'] = 'question'
    intents_dict['patterns'] = nation_question_lst
    intents_dict['responses'] = my_answer_lst + my_statement_lst
    intents_dict['context_set'] = ''
    json.dump(intents_dict, f, ensure_ascii=False, indent=4)
    f.write(',\n')

    intents_dict = {}
    intents_dict['tag'] = 'statement'
    intents_dict['patterns'] = nation_statement_lst
    intents_dict['responses'] = my_question_lst + my_statement_lst
    intents_dict['context_set'] = ''
    json.dump(intents_dict, f, ensure_ascii=False, indent=4)
    f.write(',\n')
    intents_dict = {}

    intents_dict['tag'] = 'answer'
    intents_dict['patterns'] = nation_answer_lst
    intents_dict['responses'] = my_question_lst + my_statement_lst
    intents_dict['context_set'] = ''
    json.dump(intents_dict, f, ensure_ascii=False, indent=4)
    f.write(',\n')

