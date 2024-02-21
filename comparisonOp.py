# comparison -> compare two elements 

# <> ==, etc. 

print(90 < 100)     # True or False 

# > 



# >= 
print(9 >= 9)


# ==  check for equality 

print(1 == 1)     # True
print(1 != 1)     # False
    # NOT EQUAL TO  -->  !


# combine comparison op with logical operator 
    #   -> Logical operator AND, OR, etc. 

# AND 
# True if all the conditions are true 

# COND1    COND2      RESULT 
# TRUE        TRUE      TRUE 
# TRUE        FALSE     FALSE 
# FALSE       TRUE      FALSE 
# FALSE       FALSE     FALSE 

        #  TRUE           TRUE      -> TRUE 
print(f" AND logical op: {(90 < 100) and (1 == 1)}")



# OR  
# FALSE when all conditions are false 
# COND1    COND2      RESULT 
# TRUE        TRUE      TRUE 
# TRUE        FALSE     TRUE  
# FALSE       TRUE      TRUE 
# FALSE       FALSE     FALSE 


                    #   false            true            -> TRUE 

        # f" {}"

print(" OR logical op: ", (900 < 100) or (1 == 1))
print(" OR logical op: " + str((900 < 100) or (1 == 1)))   # contenation of strings 
print(f" OR logical op: {(900 < 100) or (1 == 1)}")



# name = "joshua"
# country = "kenya"

# if name and country: 
#     if name = "joshua": 
#         print("allowed")
# print(f"name and country"  {name and country})

# decisions --> branching 

if (90>100)
print ("90 is greater than 100")
print (90+20)

