name = input("Please enter your name:")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

if age <= 18:
    print("You can Vote!")
elif age == 900:
    print("Sorry old man")
else:
    print("came back in {0} years".format(18 - age))
