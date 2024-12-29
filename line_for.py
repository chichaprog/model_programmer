"""Запись циклов for в одну строку позволяет сократить объем кода и повысить 
егo читаемость при выполнении простых операций.
Однако важно помнить
o том, что чрезмерное использование такой записи может усложнить понимание кода."""

# First model 

a = [d**2 for d in range(39)]
d = [g for g in "hello"]

print(a)
print(d)


#Second model.
#For with if.

evens = [x for x in range(10) if x % 2 == 0]
print(evens)


#Third model.
#nested loops.

pairs = [(x, y) for x in range(4) for y in range(3)]#вложеные циклы.
print(pairs)