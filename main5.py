#Feb 27, Friday, 10:00AM.
# Authors: Enkhjin, Gadiel
# Topic: Review

# def addiyion_function():
#     result = a+b
# result


# def even_or_odd(x):
    # if x % 2 ==0
    # even:

# def name_age(name,age):
#     print(f"my name is {name}, i am {age}. ")


# name_age('Enkhjin', 20)
# name_age('Gadiel', 23)

List
Length_of_the_list = len(thislist)
print(Length_of_the_list)

list_of_Supermarket = ['nomin','emart','sansar','carrefour']
for Supermarket in range (len(list_of_Supermarket)):
    print(list_of_Supermarket[Supermarket])
  
list_of_number =  [1,2,3,4,5,6,7,8,9,10 ]
def printnumber(list):
    for  number in range (len(list)):
        print(list[number])

printnumber(list_of_number)



def addnumberlist():
    limit = 5
    list_number = []
    for x in  range(limit):
        number = int(input("Enter your number:"))
        list_number.append(number)
    return list_number 

def print_list_number(list):
    for  number in range (len(list)):
        print(list[number])

def multiply(list):
    for x in range(len(list)): 
        print(list[x]*2)


my_list = addnumberlist()
print_list_number(my_list)
multiply(my_list)


#homework: 3function
#input a list of 5 fruits,print the 5 fruits of the list,if else banana or apple_ "Buy on Nomin" it is cheap otherwise buy in emart it is better 