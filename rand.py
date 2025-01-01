import random

fish = ["karas","rotan","sudak","scumbria","shark","tuna","pike","carp"]

rand_fish = []

for i in fish:
    print(i)
    n = int(input("How many times?: "))

    for a in range(0,n + 1):
        rand_fish.append(i)

fish2 = random.randint(0,len(rand_fish))
print(rand_fish)
print(rand_fish[fish2])