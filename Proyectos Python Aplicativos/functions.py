#Program to Calculate Financial Indicators for Small Business

def profit_margin(a,b): 
    
    result = a/b 
    
    if result > 0.6: 
        result = print(f"Your Profit Margin it's {result}, that means your are in a Good situation, you be part of our program about Business Digital Transformation, you have  the enough money to invest in the future of the Business")
    else: 
        result = print(f"Your Profit Margin {result} not enough to be part of the program, but we can bring a orientation and capacitation to help you  ")
    
    return result

a = float(input("Put the Net Income:"))
b = float(input("Put the Revenue:"))
    
print(profit_margin(a,b))    
