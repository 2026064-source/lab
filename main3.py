# Feb 24, Tuesday, 11:00AM.
# Authors: Enkhjin, Begu
# Topic: For Loops Advanced

odd_numbers = 0
even_numbers = 0

for x in range(0,56):
    if x % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print(f"Even numbers: {even_numbers}\nOdd numbers: {odd_numbers}")

for x in range(1,11):
    # print( 1, "x",  x, "=", x)
    print(f"1 x {x} = {x}")





num = int(input("enter number:"))

print(type(num))

if num % 2 == 0:
    print("even")
else:
    print("odd") 


