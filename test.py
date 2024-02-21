# # learing 2/9/1402
#
# # a = int(input())
# # b = int(input())
# # try:
# #     print(a/b)
# # except:
# #     print('addae dovom nemitavanad sefr bashad')
#
# import psycopg2 as cobg
#
# DB_NAME = "test"
# DB_USER = "postgres"
# DB_PASS = "postgres"
# DB_HOST = "127.0.0.1"
# DB_PORT = "5432"
#
# conn = cobg.connect(database=DB_NAME,
# 						user=DB_USER,
# 						password=DB_PASS,
# 						host=DB_HOST,
# 						port=DB_PORT)
# print("Database connected successfully")
#
# cur = conn.cursor()
# cur.execute('''
# insert into users(age, first_name, last_name)
# values(24, 'sina', 'shirazi')
# ''')
#
# conn.commit()
# print("Table updated ")
# conn.close()
# print('Connection close')
#
# # TODO join in SQL, Db diagram, Compelit 'todo_list_app'
#
import hashlib
password = '123'
h = hashlib.new('sha256')
bpass = password.encode()
h.update(bpass)
hashed = h.hexdigest()
print(hashed)