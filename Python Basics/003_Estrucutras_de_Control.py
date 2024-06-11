#Control Structures 

#Check if a Number is Odd or Even 

x = 88

if x % 2 == 0: 
    print(f"The Number {x} is Odd")
else:
    print(f"The Number {x} is Even")


products = ["A", "B", "C","D"]
prices = [200, 530, 656, 564]
costs = [120, 953, 634, 443]

portfolio = {}


for product, price, cost in zip(products, prices, costs):
    net_income = ((price - cost) * 0.9)
    if net_income > 0 :
        print(f"The Product {product} is Profitable with Net income of {net_income} ")
    else: 
        print(f"Product {product} No Profitable")
        
products_data = {}        



#While

count = 0
while count < 5:
    print(count)
    count  += 1
    
    
#Nested Loops 

i = 0
j = 0
while i < 3:
    while j < 3:
        print(f"Valor de i es: {i}, el valor de j es {j}")
        print(i,j)
        j += 1
    i += 1
    j = 0

#Christmas tree

z = 7 
x = 1

while z > 0: 
    print(" " * z + "*" * x  + " " * z)
    x += 2
    z -= 1
    
    
text = "Python"
i = 0
while i < len(text): 
    print(text[:i + 1])
    i += 1

a, b = 0, 1
while b < 25: 
    print(b)
    a, b = b, a + b
    
