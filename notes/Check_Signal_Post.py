# WAP in Python to print signal post
a = input("Enter the signal color : ").strip().lower()## strip() is used to remove any leading or trailing whitespace, and lower() is used to convert the input to lowercase for easier comparison.
if a == "red":
    print("Stop")   
elif a == "yellow":
    print("Slow down")
elif a == "green":
    print("Go ahead")
else:
    print("Invalid input")
