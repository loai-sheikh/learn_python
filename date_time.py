import datetime 
now= datetime.datetime.today()
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%Y"))
print(now.strftime("%c"))

one_day_three_hours =  datetime.timedelta(days = 1, hours = 3)

print(one_day_three_hours)
print(now)
print(now - one_day_three_hours)
print(now + one_day_three_hours)
print('***********************************')
#stopper
now_1= datetime.datetime.today()
for i in range(100000):
    pass
now_2 = datetime.datetime.today()
print (now_2 - now_1)