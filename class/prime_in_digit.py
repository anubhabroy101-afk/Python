#awp to find the prime numbers in a given number
a = int(input("Enter a number: "))
num = a
prime_digits = []
while num > 0:
    rem = num % 10
    num //= 10
    for i in range(2, rem):
        if rem % i == 0:
            break
    else:
        if rem > 1:
            prime_digits.append(rem)

print("Prime digits in", a, "are:", prime_digits)