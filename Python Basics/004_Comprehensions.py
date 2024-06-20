#Generar Lista de una Manera Más Corta y Facil de Comprender


numbers = []
for element in range (1,11):
    numbers.append(element)
print(numbers)
#Para Realizar esta lista se necesita como 3 líneas de código

#Se puede Simplificar mediante el uso de List Comprehensions
numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)
#Sintaxis más Corta y Facil de Entender
#Cumple con los principios de Python de ser Simple y Facil de Entender

numero_pares = [i for i in range(1,11) if i % 2 == 0]
print(numero_pares)

#Exercise Filter the Countries by Continent and Initial Letter
America = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

Europe  = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia & Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City']

continent = input("Enter the Continent: ").strip().title()
if continent == 'America':
    continent = America
elif continent == 'Europe':
    continent = Europe
else:
    continent = []
    print("Invalid Continent")

initial = input("Enter the Initial Letter: ").strip().upper()
search_country = [ country for country in continent if country.startswith(initial) ]

print(search_country)

#Create a List of the lengths of each word in the sentence

"""
In Python , the "split()" method is used to split a string into a list of substrings based on a specific delimiter. By Default, the delimiter is a space character.
"""

sentence = "The quick brown fox jumps over the lazy dog"
lengths = [len(word) for word in sentence.split()]
print(lengths)


# Lista de países y sus continentes
paises = [
    ("Argentina", "South America"),
    ("Brazil", "South America"),
    ("Chile", "South America"),
    ("Denmark", "Europe"),
    ("Ecuador", "South America"),
    ("France", "Europe"),
    ("Germany", "Europe"),
    ("Australia", "Oceania"),
    ("Bolivia", "South America"),
    ("Canada", "North America"),
    ("China", "Asia"),
    ("Egypt", "Africa"),
    ("India", "Asia"),
    ("Japan", "Asia"),
    ("Nigeria", "Africa"),
    ("United States", "North America")
]

# Solicitar el continente al usuario
continente_filtro = input("Enter the continent to filter by: ").title()

# Crear la nueva lista usando list comprehension
paises_filtrados = [pais for pais, continente in paises if continente == continente_filtro]

# Imprimir la nueva lista
print(paises_filtrados)


#Dictionary Comprehension
#{key: value for value in iterable}
# Method 1: Using "for" and "append"

dict = {}
for i in range(1,11):
    dict[i] = i**2

print(dict)

#Method 2: Using Dictionary Comprehension
dict_v2 = {i: i**2 for i in range(1,11)}
print(dict_v2) 
#In Dictionary Comprehension it's important to have a Key and a Value




users = ["Miguel", "Luis", "Carlos", "Juan", "Pedro"]
ages = [25, 30, 35, 40, 45]

users_dict = {i: j for i,j in list(zip(users, ages)) if j > 39}
print(users_dict)

#other way to do it
new_dict = {name: age for (name, age) in zip(users, ages) if age > 39}
print(new_dict)


#The Zip Function is used to combine two lists into a single list of tuples



text = "Í'm learning Python for Data Science"
unique = { c: c.upper() for c in text if c in "aeiou"}
print(unique)


#Now we have to count the number of vowels in the text

count_vowels = { c: text.count(c) for c in text if c in "aeiou"}
print(count_vowels)

def run():
    text = "Í'm learning Python for Data Science"
    print(text)
    unique_v2 = { c: text.count(c) for c in text if c in "aeiou"}
    print("The Count of Vowels in the Text is: ", unique_v2)

if __name__ == '__main__':
    run()

# List of Students and their grades
students = [
    ("Juan", 85),
    ("Ana", 78),
    ("Luis", 92),
    ("Maria", 66),
    ("Carlos", 74)
]

# Calculate the average grade
grades = [grade for _, grade in students]
average = sum(grades) / len(grades)
print(f"Average grade: {average}")

# Filter students with grade higher than 70
passed = [student for student in students if student[1] > 70]
print(f"Passed students: {passed}")

# Store information in a dictionary
student_info = {name: qualification for name, qualification in students}
print(f"Student info: {student_info}")