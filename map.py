words = ['apple', 'banana', 'cherry']

lengths = list(map(len, words))
print(lengths)  # Вывод: [5, 6, 6]





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