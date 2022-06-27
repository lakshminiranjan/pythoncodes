#scope - The region that var is recognised
#         A var is only available inside the region it is created
#         a globally and locally scoped versions of a variable can be created

#Python follows 
#   L-local(first)
#   E-enlosed
#   G-global
#   B-built-in

name = "Niranjan"#global scope(available in the whole program inside or outside)

def display_name():
    name = "Nizy"   #local scope (available only inside this function)
    print(name)

display_name()
print(name)