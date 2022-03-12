from typing import ParamSpecKwargs


username = input('enter your username:\n')
age = int(input('enter your age:\n'))
password = input('enter your password:\n')
if (username == '' or password == ''):
    print('user didnt enter name or password')
elif(age<18 or age>120):
    print('age not good')
elif(password != "pa$$word"):
    print('wrong password')
else:
    print('user',username, 'OK ENTER PROGRAM')
    print('program is running...')
