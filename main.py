height = int(input("Your height:"))
total = 0
if height >= 120:
    print("play")
    age =int(input("what is your age"))
    if age > 18:
        print("12 dollar")
        total = 12
    elif age > 12 and age < 18:
        print("7 dollar")
        total = 7
    elif age<12:
        print("5 dollar")
        total = 5
    picture = input("do you want your photo? Y or N: ")
    if picture == "Y":
        print("3 dollar")
        total = total + 3
    print (f"Your total is: {total}")
else: 
    print("can't play")



