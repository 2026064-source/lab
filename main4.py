#Feb 26, Thursday, 11:00AM.
# Authors: Enkhjin, Begu
# Topic: Function


def talk (): #declare
    print("hello world")

talk() #call
talk() #call
talk() #call

for x in range(1,101):
    talk()



def add(a, b):# parameter
    print(f"Addition: {a} + {b} = {a+b}")

add(2,3) #argument

# subtract()
def subtract(a,b):
    print(f"minus:{a} - {b} = {a-b}")

subtract(3,5)

square(3)
def square (a):
    print(f"square:{a} * {a} = {a*a}")

square(5)

def even_odd(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(0)




# highest(2,5) => 5

def highest(a,b):
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print("same number")
    
highest(4,4)

def highest(a,b,c):
   print(max(a,b,c))

highest(2,3,4) 

print(max(2,3,6))
# find_total(2,3,4)=>9


def find_total(a,b,c):
    print(a+b+c)
find_total(2,3,4) 
nums = [1,2,3,4,5]
print(sum([1,2,3,4,5]))
print(sum(nums))





