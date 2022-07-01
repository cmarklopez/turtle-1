

names = ["nick","katie","james"]
ages = [32,21,47]
heights = [6.1, 5.11, 5.7]

name_age = zip(names,ages,heights)

for i in name_age:
    print(i)

name_age_dict = dict(name_age)

print(type(name_age_dict))

"""Just testing some remote git stuff here."""

fruits = {'apples':123,'pears':34}
for key in fruits.keys():
    print(key, "has the value", fruits[key])



import this