#nested-function-calls = function calls inside other function calls
#                        innermost function calls are resolved first
#                        returned value is used as argument for the next 

# num = input("Enter a whole positive number : ")
# num = float(num)
# num = abs(num)#|num|- 0
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number : ")))))