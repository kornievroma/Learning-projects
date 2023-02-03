import random

names_string = input("Give me everybody's name, separated by coma. ")
names = names_string.split(", ")

num_items = len(names)

random_choise = random.randint(0, num_items -1)
person_who_will_pay = names[random_choise]

# person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal")