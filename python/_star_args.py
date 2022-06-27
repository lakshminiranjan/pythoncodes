#*args  = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


#same as varargs in java,in python we have *args-no need to neccesarily add args to *,we can add anything,"*" is imp
#args- is a tuple here
def add(*args):
    sum = 0
    args = list(args)
    args[0]=0
    for i in args:
        sum += 1
    return sum

print(add(1,2,3,4,5))