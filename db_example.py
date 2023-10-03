import sqlite3

# establish connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# sql get data query
cursor.execute("select * from events")
res = cursor.fetchall()
print(res)

# insert query
# new_rows = [('lion', 'lion city', '2023.09.11'),
#             ('tiger', 'tiger city', '2023.09.11')]
#
# cursor.executemany("insert into events values(?, ? , ?)", new_rows)
# connection.commit()