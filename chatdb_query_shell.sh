#!/bin/sh

sqlite3
.timeout 2000
.open /Users/ezulq/Library/Messages/chat.db
.timeout 2000
.output test_file_1.txt
.timeout 2000
SELECT * FROM chat;
.timeout 2000
.exit

