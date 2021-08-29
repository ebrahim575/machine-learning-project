import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from keras.models import load_model

import random
import json
import pickle
import numpy as np

import datetime
import os

# nltk.download('punkt')
# nltk.download('wordnet')

def main():
    counter = 0
    while 1:
        lemmatizer = WordNetLemmatizer()
        # intents = json.loads(open('intents.json').read(),encoding="utf-8")


        f = open('intents.json',encoding="utf-8")
        intents = json.load(f)

        words = []
        classes = []
        documents = []
        ignore_letters = ['?','!', '.',',','%']

        for intent in intents['intents']:
            try:
                for pattern in intent['patterns']:
                    word_list = nltk.word_tokenize(pattern)
                    words.extend(word_list)
                    documents.append((word_list,intent['convoNum']))
                    if intent['convoNum'] not in classes:
                        classes.append(intent['convoNum'])
            except:
                pass

        words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
        words = sorted(set(words))
        classes = sorted(set(classes))

        pickle.dump(words,open('words.pkl','wb'))
        pickle.dump(classes,open('classes.pkl','wb'))

        training = []
        output_empty = [0]*len(classes)
        for document in documents:
            bag = []
            word_patterns = document[0]
            word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
            for word in words:
                bag.append(1) if word in word_patterns else bag.append(0)

            output_row = list(output_empty)
            output_row[classes.index(document[1])] = 1
            training.append([bag,output_row])
        random.shuffle(training)
        training = np.array(training)
        train_x = list(training[:,0])
        train_y = list(training[:,1])
        # model = Sequential()
        # model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
        # model.add(Dropout(0.5))
        # model.add(Dense(64,activation='relu'))
        # model.add(Dropout(0.5))
        # model.add(Dense(len(train_y[0]), activation='softmax'))
        #
        # sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
        # model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
        #
        #
        t1 = datetime.datetime.now()

        new_chatbot_model = load_model('chatbotmodel.h5')
        hist2 = new_chatbot_model.fit(np.array(train_x),np.array(train_y),epochs=10000,batch_size=5,verbose=1) #change epochs value to train a larger quantity
        new_chatbot_model.save('chatbotmodel.h5',hist2)

        t2 = datetime.datetime.now()

        print('Time elapsed : ',t2 - t1)

main()