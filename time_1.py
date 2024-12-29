#This programm prints: day,month,year.

import datetime

res = datetime.date(2025, 12, 31)
print(res) # выведет 2025-12-31
print("day",res.day) # выведет 31
print("month",res.month) # выведет 12
print("year",res.year) # выведет 2025



#User birthday.

user_birthday = datetime.date(2013,3,14)
print("year",user_birthday.year)
print("month",user_birthday.month)
print("day",user_birthday.day)




#This programm print today date.

res = datetime.date.today()
print(res) # выведет текущую дату




#This programm prints today year,month,day.

res = datetime.date.today()
print(res) # выведет текущую дату

print("day",res.day) # выведет день
print("month",res.month) # выведет месяц
print("year",res.year) # выведет год



#Print week's day.

res = datetime.date.today()
#print(res.weekday())
print(res.isoweekday())




#This programm print time.

res = datetime.time(12,59,59)
print(res) # выведет 12:59:59

print(res.hour) # выведет 12
print(res.minute) # выведет 59
print(res.second) # выведет 59




#This prigramm prints how much time is it now.

res = datetime.datetime.now()
print(res) # выведет текущую полную дату и время
print(res.day)
print(res.month)
print(res.year)
print(res.hour)
print(res.minute)
print(res.second)




#This programm prints formated date in Python.


dt = datetime.datetime(2025, 12, 31, 12, 59, 59)
res = dt.strftime('%Y-%m-%d')

print(res) # выведет 2025-12-31


#Print epoch.

import time

res = time.time()
print(res) # выведет количество миллисекунд по текущий момент времени.


#print from epoch to date.

dt = time.time()
res = time.ctime(dt)

print(res) # выведет текущую дату



#print localtime

now = time.time()
res = time.localtime(now)

print(res)
print(res.tm_mon) # выведет 12