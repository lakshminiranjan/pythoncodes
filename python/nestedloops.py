#nested loop: a loop in a loop,The "inner loop" will finish all of its iterations before finiishing one iteration of the "outer loop"

rows = int(input("Enter the no.of rows : "))
columns = int(input("Enter the no.of columns : "))
symbol = input("Enter a symbol : ")

#outer-rows                  inner-colummns
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")#end=""---prevents the cursor from moving down to the next line
    print()