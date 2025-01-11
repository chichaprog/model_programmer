# дз
# номер 1
# дан список [1,2,3,4,5,6] чисел все числа которые равны 1, 2, 3 должны стать числом 0

array = [1,2,3,4,5,6]

def fun_1(x):
    if x in [1,2,3]:
        return 0 
    return x

# print((list(map(fun_1,array))))

print((list(map(lambda x: 0 if x in [1,2,3] else x,array))))



# номер 2
# дан список чисел и строк убрать все строки из списка

data = [1, 'hello', 2, 'world', 3, '!', 4]

print(list(filter(lambda x: not isinstance(x, str), data)))




# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой.

ar1 = [1,3,6]
ar2 = [3,9,2]


print(list(map(lambda x,y: max(x,y),ar1,ar2)))



# номер 4
# дан список в котором списки с числами ,каждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)


nested_lists = [[1, 2], [3, 4], [5, 6]]  
num = 2

result = [list(map(lambda x: x * num, sublist)) for num, sublist in enumerate(nested_lists, start=num)]
print(result)