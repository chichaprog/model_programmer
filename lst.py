#Проверяем есть объект в массиве.

array = [1,2,3,4,5,6,7,8,9,10]

a = 3 in array

print(a)



#Совмещаем два списка.

list  = [1,2,3,4,5,6,7,8,9,10] + [11,12,13,14,15,16,17,18,19,20]

print(list)

#list = [1,2,3,4,5,6,7,8,9,10]
#list2 = [11,12,13,14,15,16,17,18,19,20]
#a = list + list2
#print(a)



#Добавление значений в список.

list = ["mouse"] * 5
print(list)


#Упаковка и распаковка кортежей.

array = (one,two,three,four) = (1,2,3,4)
print(one)



#Преобразования между списками и кортежами.

a = tuple([1,2,3,4])
print(a)


a = list((1,2,3,4))
print(a) 


#Множества.

x = set([1,2,3,1,3,5])
print(x)



x = set([1,2,3,1,3,5])
x.add(6)
print(x)



x = set([1,2,3,1,3,5])
x.add(6)
x.remove(5)
print(x)



#Строки как последовательности символов.

x = "Hello"
print(x[0])
print(x[-1])
print(x)


a = len("Goodbye")
print(a)



a = 8 * "x"
print(a)



a = " ".join(["Hello,","my","name","is","Sasha"])
print(a)