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
# # to_do join in SQL, Db diagram, Completed 'todo_list_app'
#
# import hashlib
# password = '123'
# h = hashlib.new('sha256')
# bpass = password.encode()
# h.update(bpass)
# hashed = h.hexdigest()
# print(hashed)

# def parent(num):
#     def first_child():
#         return "Hi, I'm Elias"
#
#     def second_child():
#         return "Call me Ester"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# first = parent(1)
# second = parent(2)
#
# print(first)
# print(second)

#
# def test():
#     return "Hello World!"
#
# print(test())

# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#         return 5
#     return wrapper
#
#
# def say_whee():
#     print("Whee!")
#
#
# a = decorator(say_whee)
#
# b = a()
# print(b)

# from datetime import datetime
# import functools
# import time
#
#
# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__}() in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

#
# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         print(func(*args, **kwargs))
#         return func(*args, **kwargs)
#     return wrapper_do_twice
#
#
# def not_during_the_night(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if 7 <= datetime.now().hour < 23:
#            pass
#         else:
#             m = func(*args, **kwargs)
#             print(m)
#             return 'dec'
#
#     return wrapper
#
#
# @not_during_the_night
# @do_twice
# @timer
# def say_whee(name):
#     for i in range(100000000):
#         pass
#     print(f"Whee! {name}")
#     return f"return Whee! {name}"
#
# def add():
#     return 5 + 5
#
# say_whee(name='masood')
# # print(say_whee('milad'))
# # print(help(say_whee))
#
# #
# # a = not_during_the_night(say_whee)
# #
# # a()
#
#
#
# # def add(*a, **c):
# #     return c
# #
# #
# # print(add(1,2,3,3,3,4, c=4, g=5, m=87))


# def decorator(*args, **kwargs):
#     print("Inside decorator")
#
#     def inner(func):
#         # code functionality here
#         print("Inside inner function")
#         print("I like", args[0])
#
#         func()
#
#     # returning inner function
#     return inner
#
#
# @decorator("geeksforgeeks")
# def my_func():
#     print("Inside actual function")


# class Nothing:
#     @staticmethod
#     def a():
#         print('hello world')
#
#
# m = Nothing()
# m.a()

# from dataclasses import dataclass
#
#
# @timer
# @dataclass
# class TimeWaster:
#     max_num: int
#
#     def waste_time(self, num_times):
#         for _ in range(num_times):
#             i = sum([i**2 for i in range(self.max_num)])
#         print(i)
#
# a = TimeWaster(100)
# a.waste_time(100000)



from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
    return {"name": name, "age":age}
@app.get("/hello")
async def hello(name:str,age:int):
    return {"name": name, "age":age}

@app.get("/hello/{name}")
async def hello(name:str=Path(...,min_length=3,
max_length=10)):
    return {"name": name}
