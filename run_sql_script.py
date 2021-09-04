# import os
# import subprocess
#
# subprocess.run(["ls"], capture_output=True)




import subprocess

path = '/Users/ezulq/Library/Messages/chat.db'

process = subprocess.Popen(['sqlite3','.open /Users/ezulq/Library/Messages/chat.db','SELECT * FROM chat'])

out = process.communicate()
print(out)

#
# os.system('sqlite3')
# os.system('.open ',path)

# SELECT
#     datetime (message.date / 1000000000 + strftime ("%s", "2001-01-01"), "unixepoch", "localtime") AS message_date,
#     message.text,
#     message.is_from_me,
#     chat.chat_identifier
# FROM
#     chat
#     JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id
#     JOIN message ON chat_message_join.message_id = message. "ROWID"
# WHERE
# 	chat.chat_identifier = '+16307858333'
# ORDER BY
#     message_date DESC;