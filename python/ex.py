a = "q"
u,l,d,s = 0,0,0,0

print("Enter * to exit")

while len(a) == 1:
    name = input("Enter any character:")
    if (name == "*"):
        break
    elif(name >="a" and name <="z"):
        l+=1
    elif(name >="A" and name <="Z"):
        u+=1
    elif(name >="0" and name<="9"):
        d+=1
    else:
        s+=1
        if(name == "*"):
            s = s-1

print("Total count of lower case : "+str(l)+" "+"Total count of uppercase : "+str(u)+" "+"Total count of special characters : "+str(s)+" "+"Total count of digits: "+str(d))