#Control Structures 

#Check if a Number is Odd or Even 

print("*" * 7 + "Control Structures" + "*" * 7)

print("/" * 7 + "1. IF" + "/" * 7)

x = 88

if x % 2 == 0: 
    print(f"The Number {x} is Odd")
else:
    print(f"The Number {x} is Even")


print("/" * 7 + "2. FOR & IF" + "/" * 7)

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
print("/" * 7 + "3. WHILE" + "/" * 7)

count = 0
while count < 5:
    print(count)
    count  += 1
    
#While with else
print("/" * 7 + "4. WHILE & ELSE" + "/" * 7)

#Data to complete The Project
Investment = int(input("Enter the investment amount: "))
current_assets = 1200
current_liabilities = 890
operating_costs = 5570
working_capital = current_assets - current_liabilities + Investment
max_bank_financing = 0.5 * current_assets
startup_value = 6000
share_value = startup_value/100
max_percent_sell = 20
max_income_shares = max_percent_sell * share_value

print("*"*20)
print("Data")
print("*"*20)
print(f"Initial investment: {Investment}")
print(f"Current assets: {current_assets}")
print(f"Working capital: {working_capital}")
print(f"Max bank financing: {max_bank_financing}")
print(f"Max income from shares: {max_income_shares}")
print(f"Operating costs: {operating_costs}")
print("*"*20)

#Sources of Financing
bank_financing = 0
percent_sell = 0
income_shares = 0
financial_requirements = operating_costs - working_capital
other = 0


# Loop to seek financing
x = 0
while working_capital + bank_financing + income_shares + other < operating_costs:
    print(f"Current working capital: {working_capital}, additional {financial_requirements} needed to cover operating costs.")

    # Attempt to secure bank financing if necessary
    if bank_financing < financial_requirements and bank_financing < max_bank_financing:
        to_borrow = min(max_bank_financing, financial_requirements - bank_financing)
        bank_financing += to_borrow
        financial_requirements -= to_borrow
        print(f"Bank financing secured: {to_borrow}")

    # Attempt to sell shares if necessary
    if income_shares < financial_requirements:
        if max_income_shares < financial_requirements:
            income_shares += max_income_shares
            print(f"Shares sold: 20% of the company (Total income from shares sold: {income_shares})" )
            other = financial_requirements - income_shares
            print(f"We need {financial_requirements}, so we've to Find other ways to finance the project")
        else:
            income_shares = financial_requirements 
            shares_to_sell = income_shares / share_value
        
            print(f"Shares sold: {shares_to_sell} (Total income from shares sold: {income_shares})" )

    x += 1
else:
    print(f"Financing secured after {x} iterations.")
    print(f"Total bank financing secured: {bank_financing}")
    print(f"Total income from shares sold: {income_shares}")
    print(f"Total other financing: {other}")



print("*"*20)
print("/" * 7 + "5. NESTED LOOPS" + "/" * 7)
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
    
#SWITCH CASE
#Concepts 
#Switch is a tool that allows us to execute different sections of a code depending on a condition. It´s functionality id similar to using multiple "if´s". In Python, we don´t have a switch statement, but we can use the elif statement to achieve the same result.
# Switch = elif

i = int(input("Enter a number between 1 and 5: "))
v = ["a","e","i","o","u"]
o = ["first","second","third","fourth","fifth"]
if i == 1:
    print(f"the {o[i-1]} vowel is {v[i-1]}")
elif i == 2:
    print(f"the {o[i-1]} vowel is {v[i-1]}")
elif i == 3:
    print(f"the {o[i-1]} vowel is {v[i-1]}")
elif i == 4:
    print(f"the {o[i-1]} vowel is {v[i-1]}")
elif i == 5:
    print(f"the {o[i-1]} vowel is {v[i-1]}")
else:
    print("Invalid number")