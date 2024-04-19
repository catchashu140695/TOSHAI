import sqlite3

conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()

# query="insert into sys_command values(null,'download manager','C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe')"
# cursor.execute(query)
# conn.commit()