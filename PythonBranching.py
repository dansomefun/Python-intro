# Making decisions, evaluate decisions  
# if, elif and else 

# if  
# if condition:                True
#     statement1 
#     statement2
 
    #  TRUE 
if 90 > 100:
    print("90 is less than 100")
    print(90 + 100)
else: 
    print("90 is NOT less than 100")


# if, elif, else 
day = "Friday"


if day == "Monday": 
    print("Today is Monday")
elif day == "Friday": 
    print("Today is 1st Friday")
elif day == "Wednesday": 
    print("Today is Wednesday")
elif day == "Friday": 
    print("Today is Friday")
else: 
    print("Today is Sunday")


    # NESTED IF  
num = 9

# (9/2) -> 4.5
# 9%2 

if num%2 == 0:
    print("Even Number")
    if num%3 == 0: 
        print("Divisible by 3")
    else: 
        print("NOT Divisible by 3")

else: 
    print("Odd Number")
    if num%5 == 0: 
        print("Divisible by 5")
    else: 
        print("NOt Divisible by 5")





# SHORTHAND IF  
if 90 > 100:
    var = "90 is less than 100"
else: 
    var = "90 is NOT less than 100"

print(var)