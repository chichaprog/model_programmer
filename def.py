#Programm with def sum.

def sum(a,b):
    c = a + b
    return c
print(sum(1,2))



#Programm with def minus.

def minus(a,b):
    c = a - b
    return c
print(minus(3,2))



#Array sum.

array = [1,2,3,4,5,6,7,8,9,10]

def array_sum(array):
    s = 0
    for a in array:
        s += int(a)
    return s

print(array_sum(array))



#Mul_table def.

def mul_table():
    for i in range(2,11):
        print(i,end = "\t")

    for i in range(2,11):
        print()
        for j in range(2,11):
             print(i * j,end = "\t")

print(mul_table()) 



#Sum and teplay

def unifirsul(a,b,c):
    sum = a + b * c
    return sum

print(unifirsul(12,3,5))



#A lot of func

def unifirsul_dif(a,b,c,d):
    dif = a // b % c * d
    return dif

print(unifirsul_dif(100,2,4,56))



#Func model school math excercise.

def math_model(a,b,g,h,k):
    exercise = ((a + b) + (g * h)) // k
    return exercise

print(math_model(39,39,5,8,2))



#Func for step 1.

def math_excercise2(a,b):
    step = a**2 + b**2
    return step

print(math_excercise2(4,3))



#Func for step 2.

import math

def math_sqrt(a,s):
    return math.pow(a, 1/s)

print(math_sqrt(64,3))



#chat_prigrammer.

def chat_robot():
    print("Hello, I am robot.")
    print("My name is Mark.")

    print("What is your name?")
    name = input("")

    print(name,"Nice to meet you.")
    print("how are you?")
    react = input("")

    print("What is your hobby?")
    hobby = input("")

    print(hobby,"is cool.")
    print("Do you like play",hobby)
    hobby = input("")
    print("Good")
    print("Becouse do you like play")
    hobby = input("")
    print("ok")

    print("What language  do you know?")

    language = input("")
    print("Do you speak well for this language or languages")
    language = input("")


    print("Do you work?")
    work = input("")
    print("What is your profession?")
    work = input("")
    print(work,"is cool.")
    print("what do you like about your work?")
    work = input("")
    print(work,"Good.")
    print("Do you have friends at work?")
    work = input("")

    if work.lower() == "Yes I have".lower():
        print("Exactly how many friends do you have?")
        work = input("")

        many_friends = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
        for i  in many_friends:
            if int(work) == i:
                print(work,"Really? You have so many friends?")
                print(work,"Ok")

    if work.lower() == "No I don't have friends".lower():
        print("sorry")
        print("or maybe you have a friend at work?")
        work = input("")

    if work.lower() == "No I don't have".lower():
        print(work,"Very bad")

    print("What is your salary?")
    work = input("")
    print("Ok")

    print("Is your family big?")
    family = input("")

    if family.lower() == "Yes".lower():
        print("Good")
    
    if family.lower() == "No".lower():
        print("Ok")

    People_family = {"granny","grandad","father","mother","brother","sister"}

    print("Who is in your family?")
    family = input("").lower()
    print(family)
    if family in People_family:
        print("Ok")
    
    print("Do you have car?")
    car = input("")
    if car.lower()  == "Yes I have".lower():
        print("Good")
        print("What brand is it?")
        car = input("")
        print(car,"ok")
        print("Is your car old?")
        car = input("")
        print("OK")
    
    if car.lower() == "No I haven't".lower():
        print("This bad")

    print("Where do you live?")
    live = input("")

    if live.lower() == "I live in city".lower():
        print("What is the name of your city?")
        live = input("")
        print("Ok")
    
    if live.lower() == "I live in town".lower():
        print("What is the name of your town?")
        live == input("")
        print("Ok")

    print("Bye.")
    print("See you later.")

chat_robot()


#number hip. 

def hip_number(a,b):
    hip = a**2 + b**2
    return hip

print(hip_number(4,3))



#Array.

x = [2, "two","three","four","five", [1,2,3,4,5,6,7,8,9,10]]
print(len(x))




#New chat robot.

def chat_robot():
    print("Hello, I am robot.")
    print("My name is Mark.")

    print("What is your name?")
    name = input("")
    print(f"{name}, nice to meet you!")

    print("How old are you?")
    age = int(input(""))
    if age > 20:
        print("You are adult")

    print("How are you doing today?")
    react = input("")

    print("What is your favorite hobby?")
    hobby = input("")
    print(f"{hobby} sounds really interesting!")

    print(f"Do you enjoy playing {hobby}?")
    likes_hobby = input("")
    if likes_hobby.lower() in ["yes", "yeah", "y"]:
        print("That's awesome! What do you like most about it?")
        hobby_enjoyment = input("")
        print(f"{hobby_enjoyment} sounds fun!")

    print("Which languages do you speak?")
    language = input("")
    print("Do you consider yourself fluent in that language?")
    speak_level = input("")

    print("Are you currently employed?")
    work_status = input("")

    if work_status.lower() in ["yes", "yeah", "y"]:
        print("What is your job title?")
        profession = input("")
        print(f"{profession} is a great profession!")

        print("What do you enjoy about your job?")
        work_likes = input("")
        print(f"{work_likes} is a good reason to love your job.")

        print("Do you have friends at work?")
        friends_at_work = input("")

        if friends_at_work.lower() in ["yes", "yeah", "y"]:
            print("How many friends do you have at your workplace?")
            friend_count = int(input(""))
            if friend_count > 0:
                print(f"{friend_count} friends? That's fantastic!")
            else:
                print("That's okay! Sometimes it's about quality over quantity.")

        else:
            print("Sorry to hear that. Do you at least have a colleague you're close with?")
            friend_option = input("")
            if friend_option.lower() in ["yes", "yeah", "y"]:
                print("That's great to hear!")
            else:
                print("I hope you'll make some friends soon.")

        print("What is your monthly salary?")
        salary = input("")
        print("Is that sufficient for your needs?")

    else:
        print("What do you spend your time on instead of working?")

    print("Is your family large or small?")
    family_size = input("")

    people_family = ["granny", "grandad", "father", "mother", "brother", "sister"]

    print("Who are the members of your family? (You can list them)")
    family_members = input("").split(", ")

    for member in family_members:
        if member.lower() in people_family:
            print(f"{member.capitalize()} is a lovely family member!")
        else:
            print(f"{member.capitalize()} sounds interesting!")

    print("Do you own a car?")
    car_status = input("")

    if car_status.lower() in ["yes", "yeah", "y"]:
        print("Great! What brand is it?")
        car_brand = input("")
        print(f"{car_brand} is a nice choice!")

        print("Is your car old or new?")
        car_age_status = input("")

    else:
        print("That's okay! Public transport can be very convenient.")

    print("Where do you live? (City, town, etc.)")
    live_status = input("")

    if live_status.lower() in ["in a city", "city"]:
        print("What is the name of your city?")
        city_name = input("")
        print(f"{city_name} must be a vibrant place!")

    elif live_status.lower() in ["in a town", "town"]:
        print("What is the name of your town?")
        town_name = input("")
        print(f"{town_name} sounds lovely!")

    # New questions added
    print("What is your favorite food?")
    favorite_food = input("")

    print(f"{favorite_food} sounds delicious! Do you like cooking it yourself?")
    likes_cooking = input("")

    if likes_cooking.lower() in ["yes", "yeah", "y"]:
        print("That's awesome! What's your favorite dish to cook?")
        favorite_dish = input("")

    else:
        print("No worries! Sometimes it's nice to eat out.")


# Additional questions about travel
    print("Have you traveled anywhere interesting recently?")
    travel_experience = input("")

    if travel_experience.lower() in ["yes", "yeah", "y"]:
        print("Where did you go?")
        travel_destination = input("")

        print(f"{travel_destination} sounds amazing! What did you enjoy most about it?")

    else:
        print("Maybe you have plans to travel soon?")

    # Closing the conversation
    print("Thank you for chatting with me!")
    print("Goodbye! See you later.")


chat_robot()