#tuple----() immutable
#collection which is "ordered" and unchangeable used to grp together related data-mostly used to grp diff data types of same grp
#default list will be tuples

student = ("Niranjan",21,"Male")

print(student.count("Niranjan"))#counts that how many times the value is repeated
print(student.index("Male"))

for i in student:
    print(i)


if "Niranjan" in student:
    print("Niranjan is present")