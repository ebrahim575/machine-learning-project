import sqlite3
def get_data():
    conn = sqlite3.connect('/Users/ezulq/Library/Messages/chat.db')
    cur = conn.cursor()
    #cur.execute(\"SELECT * FROM chat\")
    cur.execute(
    "SELECT datetime (message.date / 1000000000 + strftime (\"%s\", \"2001-01-01\"), \"unixepoch\", \"localtime\") AS message_date, \
        message.text, \
        message.is_from_me, \
        chat.chat_identifier \
    FROM \
        chat \
        JOIN chat_message_join ON chat. \"ROWID\" = chat_message_join.chat_id \
        JOIN message ON chat_message_join.message_id = message. \"ROWID\" \
    WHERE \
        chat.chat_identifier = '+16307858333' \
    ORDER BY \
        message_date DESC;")
    data = cur.fetchall()
    return data
def get_text():
    data = get_data()
    for i in range(len(data)):
        #print(data[i])
        if data[i][2] == 0:
            return data[i][1]


