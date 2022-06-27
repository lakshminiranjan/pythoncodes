#exception - events detected during execution that interrupts the flow of program
#  in java       try    catch    finally
# in  python     try    except   finally
try:#acts as if
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter Denominator: "))
    result = numerator / denominator



except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")

except ValueError as e:
    print(e)
    print("Enter only numbers please!...")
except Exception as e:#optional if upper both cases fails then this comes into attack
    print(e)#prints the specific exception computer itself without any manual thing
    print("Something went wrong :(")

else:#prints the res only if no error occurs
    print(result)


finally:#it doesn't care if the above blocks executes or not it will just execute
    # print("This will always execute")
    print("Hello NIZY!")