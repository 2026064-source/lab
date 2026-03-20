#dictionary

Enkhjin_information = {
    "Name" : "Enkhjin",
    "Nationality" : "Mongolia",
    "faviourate_color" : "sowty_color",
}
Enkhjin_nationality = Enkhjin_information["Nationality"]
print(Enkhjin_nationality)
Enkhjin_nationality2 = Enkhjin_information.get("Nationality")
print(Enkhjin_nationality2)
key = Enkhjin_information.keys()
print(key)
value = Enkhjin_information.values()
print(value)
Enkhjin_information["Nationality"] = "USA"
print(Enkhjin_information)
Enkhjin_information["Year"] = "2005"
print(Enkhjin_information)
Enkhjin_information["Brothers"] = 1
# Enkhjin_nationality.update({"Brothers": 1})
print(Enkhjin_information)



# for i in Enkhjin_information:
#     print(i) #keys
#     print(Enkhjin_information [i]) #values

# for x, y in Enkhjin_information.items():
#     print(f"key: {x}, Value:  {y}")

# Removing:
Enkhjin_information.pop("Brothers")
for i in Enkhjin_information:
    print(i)
