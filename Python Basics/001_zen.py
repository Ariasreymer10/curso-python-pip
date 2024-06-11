#ZEN - PYTHON 

#import this

"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

#Beautiful is Better than Ugly

#Feo 
def operation(a,b):
    result=(a**2+b**2)/(a*b)
    return

#Beautiful Se di
def operation(a,b):
    numerator = a**2+b**2
    denominator = a*b
    result = numerator/denominator
    return result

#In rhe Beautiful Version of the code breaks down the "operation" into simpler and clear steps, usign descriptive variable names, making the code more readable and easier to understand


#Explicit is Better than Implicit

#Implicit
def calculate_price(base_price): 
    tax = base_price * 0.12
    return base_price + tax

#Explicit
def calculate_price(base_price): 
    tax_percent = 0.12
    tax = base_price * tax_percent
    final_price = base_price + tax
    return final_price
#"Explicit" Version of the Code makes it Clear thats tax is 12% of the base price

#Simple is better than complex 

#Complex
def find_element(list,element):
    if element in list:
        index = list.index(element)
        return index
    else: 
        return -1


#Simple
def find_element(list,element):
    try:
        index = list.index(element)
        return index
    except ValueError: 
        return -1
    