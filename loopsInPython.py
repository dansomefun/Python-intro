# FOR LOOPS & WHILE LOOPS 
# for loops  
# -> allow you to iterate through a sequence -- list

            # 34^2 
list_val = [34, 2, 56, 90]
# list_val[0]*
                
                # (length of the seq)
for i in list_val: 
    # print("morning")
    print(i)

# print("this is the final temporary variable: ", temp_var)


for i in list_val: 
    sq = i ** 2
    print(sq)




# None datatype  --> absence of value
# empty_list = []
# empty_list.append("phone")

# print(empty_list)


square_list = []
        # [34, 2, 56, 90]
for i in list_val: 
    sq = i ** 2 
    # add = i + 30
    square_list.append(sq)


print(square_list)


# for loop & dictionaries 

dict_val = {"samsung": 1200, 
            "iphone": 1300, 
            "xiaomi": 600}


print(dict_val.items())
# print(dict_val.keys())
# print(dict_val.values())


for val in dict_val.values(): 
    print(val)



                            # ('samsung', 1200)
                            # ('iphone', 1300)
                            # ('xiaomi', 600)
for item, price in dict_val.items(): 
    # print(item, price * .3)
    print(item, price ** 2)


# enumerate() 
for index, val in enumerate(dict_val.values()): 
    print(index, val)

# zip()
fruits = ["mango", "apple", "pineapple"]
country = ["cambodia", "us", "oceania"]

for fruit, price, country in zip(fruits, dict_val.values(), country): 
    print(fruit, price, country)


# WHILE LOOPS -> continually performing an action
                                    #    until some condition is met

# while condition:     --> TRUE
#     statement1



num = 1 

# while num < 5: 
#     print(num, "is less than 5")

while num < 5: 
    print(num, "is less than 5")

    num = num + 1 
            

#Personal training by AYOOLA
if 90 > 100
    print ("90 is greater than 100")
    print(90+100)

