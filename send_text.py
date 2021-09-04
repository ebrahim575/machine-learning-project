# import os
# import time
#
# def get_words(file_path):
#     with open(file_path, 'r') as f:
#         text = f.readlines()[0]
#         words = text.split()
#     return words
#
# def get_lines(file_path):
#     with open(file_path, 'r') as f:
#         text = f.readlines()
#     return text
#
# def send_message(phone_number, message):
#     os.system('osascript send.scpt {} "{}"'.format(phone_number, message))
#
# if __name__ == '__main__':
#     counter = 0
#     # words = get_words('scriptTest.txt')
#     # for word in words:
#     #     send_message("6303634339", word)
#     #     time.sleep(5)
#
#         #counter = counter + 1
#         #if counter == 10:
#         #   break
#         #counter limits the amount of texts that can be sent
#
#     text = get_lines('keplar.txt')
#     for line in text:
#         send_message("16303634339", line)
#         time.sleep(60)
#         counter = counter + 1
#         if counter == 199:
#             break
#         # counter limits the amount of texts that can be sent

from sql_query import *
import os

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))
