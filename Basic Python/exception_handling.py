x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

try:
    z = x/y
except Exception as e:  # except ZeroDivisionError as e

    print("An exception has occured ",e)
    z = None
else:
    print(z)
    print("no exception")
finally:
    print("try block completed ")
    print(z)



