#lesson number 1.

# операторы присваивания 
# print(4)
# num = 7
# num = 2
# num = num + 8
# num += 2
# num -= 2

# num_2 = None



# получаем тип
# print(type(num))



# типы
# print("int" , 5)
# print("float" , 5.0)
# print("str" , "text")
# print("bool" , True)
# print("null" , None)



# получаем символ строки через for
# str_a = "hello"
# print(str_a)
# for sym in str_a:
#     print(sym)




# функция это переменная
# def fun_1() -> str:
#     print("hello")
#     return 4

# print(fun_1)
# print(type(fun_1))
# print(fun_1())




# def fun_2(x:int):
#     return 4 * x
# print(fun_2(" wert"))





num = 8
def fun_3():
    # создаем свою локальную переменную num
    num = 20
    print(num)
fun_3()
print("num =" , num)




# # num = 8
# def fun_4():
#     # изменение глобальной переменной в функции
#     global num
#     num = 20
#     print(num)
# fun_4()
# print("num =" , num)




# у каждой функции своя локальная переменная
# num = 8
# def fun_5():
#     # print("fun4_1 =" , num)
#     num = 20
#     print("fun4_2 =" , num)
#     def fun6():
#         # print("fun5_1 =" , num)
#         num = 30
#         print("fun5_2 =" , num)
#     fun6()

# fun_5()
# print("num =" , num)




# def fun_4():
#     # создание глобальной переменной в функции
#     # global num
#     num = 20
#     print(num)
# fun_4()
# print("num =" , num)



#lesson number 2.





# создание словаря
obj = {
    "key":30,
    "255":"wffff",
    "qwe":[1,2,4],
    488:"wdw",
}
# print(obj)
# получаем значение по ключу
# print(obj["255"])



# словарь это список
# obj_arr = {
#     0:1,
#     1:30,
#     2:50,
#     3:300,
# }
# print(obj_arr[2])



# metods:

# очищает словарь
# obj.clear()
# obj = ""
# print(obj)



# возвращает копию словаря
# obj.copy()


# пример зачем нужна копия
# obj_2 = obj
# print("obj =" , obj)
# print("obj_2 =" , obj_2)
# obj.clear()
# print("obj =" , obj)
# print("obj_2 =" , obj_2)



# меняем значение по ключу
# obj["qwer"] = 9
# print(obj)



# метод get возвращает значение ключа, но если его нет возвращает None
# print(obj["123"])
# print(obj.get("key"))
# print(obj.get("123"))



# метод setdefault(key, val) - возвращает значение key, но если его нет создает key со значением val или None
# print(obj.setdefault("key"))
# print(obj.setdefault("123"))
# print(obj.setdefault("123" , 999))
# print(obj.setdefault("key" , 999))

# print(obj)



# удаляет по ключу и возвращает значение
# print(obj.pop("qwe"))
# print(obj)



# удаляет последнюю пару и возвращает её
# print(obj.popitem())
# print(obj)



# возвращает список ключей
# print(obj.keys())
# print(list(obj.keys()))



# возвращает список значений
# print(obj.values())
# print(list(obj.values()))



# обедняет два словаря 
# obj.update({
#     0:23,
#     "oos":5678907
# })

# print(obj)



# создаёт разные ключи с одним значением 
# print(obj.fromkeys([1,2,3,5] , 20))



# метод items позволяет for перебирать ключ и значение словаря
# for key , val in obj.items():
#     print(key , "=" , val)






# способ использования словаря
# inp = input("=== ")
# num = None
# if(inp == "q"):
#     num = 1
# elif(inp == "w"):
#     num = 2
# elif(inp == "e"):
#     num = 3
# elif(inp == "r"):
#     num = 4
# elif(inp == "t"):
#     num = 5
# print(num)



# замена if для краткого написания
# obj_if = {
#     "q":1,
#     "w":2,
#     "e":3,
#     "r":4,
#     "t":5,
# }
# num = obj_if[inp]
# print(num)




#lesson number 3.


