#keyword_arguments = arguments preceded by an "identifier" when we pass them to a function(argument value sent to the function)
#                    the order of the arguments does not matter,unlike positional arguments
#                    python knows the names of th arguments that our function recieves


def hello(first,middle,last):
    print("Hello ",first,"",middle,"",last)

hello(last="PUCCHAGINJALA",first="LAKSHMI",middle="NIRANJAN")#keyword arguments
hello("first", "middle", "last")#positional arguments