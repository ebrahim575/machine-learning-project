import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model


lemmatizer = WordNetLemmatizer()

f = open('intents.json',encoding="utf-8")
intents = json.load(f)

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbotmodel.h5') #model = load_model('chatbot_model.model')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words) #empty array filled with 0 of size of arr
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.35
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD] #0 should be "ERROR_THRESHOLD (temp value since we are training still
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability': str(r[1])})
    #print(return_list)
    return return_list

def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['convoNum'] == tag:
            result = random.choice(i['responses'])
            break
    return result

while 1:
    print()
    message = input('What would you like to say? : ')
    ints = predict_class(message) #ints comes out as an empty list
    res = get_response(ints,intents)
    print(res)