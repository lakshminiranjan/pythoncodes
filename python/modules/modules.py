#modules = a file containing python code.May contain functions ,classes etc
#used with modular programming, which is to seperate a program into parts

# import messages as msg#messages =====msg here
# from messages import hello,bye#by using this we don't need to use module.hello()-- can directly write hello()
from messages import *#import all the functions of the module messages--not suggested

# msg.hello()
# msg.bye()

hello()
bye()


help("modules")#gives the list of all inbulid modules of python