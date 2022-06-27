#and or not -used to verify two or more conditions within a single block of code
# flip the statement codition true to false and false to true 

temp = eval(input("Enter the temperature: "))

if not(temp >=0 and temp <=30 ):#both must be true
    print("Temperature is bad today,Stay inside")

elif not(temp <0 or temp >30):#only one can be
    print("Temperature is good today,Can go outside")

