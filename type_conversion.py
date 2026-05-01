# 🌟 type conversion

# Implicit type conversion (automatic type conversion)

a = 2
b = 4.25
sum1 = a+b
# a (int type) is converted to float type before addition (float is the higher data type)
print("a+b =", sum1, "and the type of sum1 is", type(sum1))
# ERROR‼: a (int type) cannot be added to a string type
# print("a + 'Hello' =", a + 'Hello')  # This will raise a TypeError because you cannot add an integer and a string together

# Explicit type conversion (manual type conversion)

c, d = 5, '3.14'
e = float(d)  # Convert string to float
sum2 = c + e  # Adding the converted float
print("c + d =", sum2, "and the type of sum2 is", type(sum2))
# ERROR‼: d (string type) cannot be converted to an integer or float type
# print("c + int(d) =", c + int(d))  # This will raise a ValueError because '3.14' cannot be converted to an integer
