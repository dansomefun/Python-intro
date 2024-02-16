print("hello")

print(34)

# variable name    assignment operator    value
var_name                    =           "Ayoola"

# comparison operators  
# ==     # equal sign 
print(var_name)


            # PYTHON DATA TYPES 
# 1. Primitive data types (hold single values)
# integer  - whole number values (i.e positive or negative)
print(1)
# string - character and rep with quotes ""
name = "Ayoola"

# float 
print(1.0)
# boolean -> rep of two values: True or False 
print('o' in name)
#  output -> True

# None -> absence of value

val = None

val = 678

print(val)

# empty_list = []
# empty_dict = {}


 
# 2. Data Structures/ Containers  (hold multiple values)
# List 
# tuple
# dictionary 
# set 



# A. LIST -> ordered collection of items []

      #    0    1   2  3 
        # -4    -3  -2 -1
num_list = [23, 45, 6, 8]

# indexing 
print(num_list[1])
print(num_list[-1])


# slicing 
print(num_list[0:1])
print(num_list[-3:-1])


# reassigning items in a list 

num_list[3] = 70

print(num_list)



# NESTED LIST -> list inside a list
            #  0        1         2        3
            #                            0    1  2  3
            #                           [23, 45, 6, 70]
nested_list = ["mango", "apple", "dates", num_list]


    # indexing a nested list 
print(nested_list[3][2])

print(nested_list[3][-1])

 # slicing a nested list 

print(nested_list[1:])
print(nested_list[3][1:3])
                # 0   2      2
                #             0        1       2         3
                                                  #    0    1   2   3/-1
  #                                                    [23, 45, 6, 70]
                    #    ["mango", "apple", "dates", num_list]
another_list = [34, 45, nested_list]
print(another_list)
print(another_list[2][3][-1])

# reassignment in a nested list --> reassign no. 45 with "pineapple"
another_list[2][3][1]= "pineaple]"
print(another_list)


# methods in list -> specific functions to a datatype
# print(23) ->output 23 

# .append()  -> add a value to a list 
                #  0         1         2
electronics = ["laptop", "phone",  "headphone"]
electronics.append("microphone")

# .insert() 
# .insert(position, value)

electronics.insert(2, "tv")

print(electronics)


# .pop()  
print("popped out value:", electronics.pop(2))

print("popped last value: ", electronics.pop())  #  -> remove the last value
print(electronics)

# .remove()
electronics.remove("headphone")


print(electronics)

# concatenation in strings  +
print("mango " + "juice")     # mangojuice


# contatenation in lists

concat_list = electronics + [45, 56, 78]

print(concat_list)


        # B. TUPLES -> ordered collection of items  ()   comma ,
                #    -> IMMUTABLE (CANNOT BE CHANGED)

       #     0    1   2
tuple_val = (34, 56, 7)


# indexing 
print(tuple_val[1])

# slicing 
print(tuple_val[1:])


# tuple unpacking 

name_1, name_2 = "Ayoola", "Abok"


countries =  ("Kenya", "Tanzania")
print(countries)  

num = 45

print(num)

# type() function 
print(f"type of number value: {type(num)}")

        # f-string  
print("type of number value:", type(num))

# use tuple() function 
# print()
print(tuple([23, 45, 67]))









# type() function 

# ()  []   {} , 

# list -> []
# tuple -> ()
# dictionary -> {}
# print(name_2)








# C. DICTIONARY -> UNordered collection of items {}

# rep key and value pairs  

dict_val = {
            "key2": "value2", 
            "key1": "value1"}


# print(dict_val["key1"])
# print(dict_val["key2"])


dict_countries = {1: "Israel", 
                  2: "UK",
                  56: "Japan"}


print(dict_countries[56])

print(dict_countries.get(2))


# reassignment in dictionaries
dict_countries[1] = "Tanzania"


# add values 
dict_countries[90] = "Nigeria"

print(dict_countries)




# methods in dictionary 

# remove values -> .pop()  
print(dict_countries.pop(1))
print("dictionary after pop: ", dict_countries)


# key only -> dict_val.key()
print("dictionary keys:", dict_countries.keys())

# value only -> dict_val.value()

print("dictionary values:", dict_countries.values())

# both key and value 
print("dictionary items:", dict_countries.items())


        # D. SETS -> collection of unique items {}

list_new_values = [23, 45, 7, 8, 7, 23, 2, 2, 3, 3]
set_val = {23, 45, 7, 8, 7, 23, 2, 2, 3, 3}

print(f"our list values: {list_new_values} \n our set values: {set_val}")
# f-string   f" something {}"

# methods in sets 
# .add()
set_val.add(57)
print(set_val)

# .intersection 

new_set = {23, 4, 7}


set_val.intersection(new_set)
# .pop()

print(set_val.pop())

# .clear

# set_val.clear  





"""
Question 4:
----------

Write a Python program to split the words in the sentence. 
And then print the length of the of the words created."""

sentence = "Python is an awesome language"
# string data type  -> method in string
# .split()
words = sentence.split("is")

tweet_data =  "sports is great #football #sunday".split("#")
print(tweet_data)


# len()  print()  type() -> type of a object 
print("len of sentence: ", words)
print("len of sentence: ", len(words))
# print(sentence)
