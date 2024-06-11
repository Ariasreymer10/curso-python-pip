#Sets & List & Tuples 

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_other_list))


# The values that are contained in the list are assigned to different Variables

age, height, name, surname = my_other_list

print(name)


#Other Way to Assigned the values in to teh different Variables more accurately using index

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[-1]

print(surname)

my_list = ["Miguel", 23]

#Concatenation 

print(my_other_list + my_list)


# Create, insert, update and Remove
my_list.append("ariasreymer10@gmail.com")
my_list.append("Arequipa")
my_list.append("Peru")
my_list.append("Industrial Engineer")

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)


startup = ["Microsoft","Googles","OpenAI","Apple"]
chatbot_Ai = ["Copilot","Gemini","ChatGpt","Siri"]

for index,s in enumerate(startup):
    print(f"This are the Leading Companies in AI, in the index {index} est la empresa: {s}")

for s, c in zip(startup,chatbot_Ai):
    print(f"{s}'s Artificial Intelligence Chatbot is {c}")

#Dictionary

dict = {}
for i in range(1, 5):
  dict[i] = i * 2 #Cómo es una llave de valor se debe añador su I o llave de valor

print(dict)

numbers = {}
for i in range(5,10):
    numbers[i] = i*2 
print(numbers)

cars = ["Mercedes","Ford", "Ferrari", "GMC"]

prices = [70000,20000,100000,40000]

brand_price = {}

for car,price in zip(cars,prices):# Zip esta emparejando elementos de amabs listas
    brand_price[car] = price

print(brand_price)

dict_v2 = {i:i*2 for i in range(5,10)}
print(dict_v2)

import random 

cities = ["Arequipa", "Lima", "Cusco"]

population = {}
for city in cities:
    population[city] = random.randint(50,200)
print(population)


population_v2 = {city: random.randint(50,200) for city in cities}
print(population_v2)

result = {city:population for (city, population)in population_v2.items() if population > 100 }

print(result)



    








