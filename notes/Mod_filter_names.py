#Filter names starting with a given character

n = int(input("Enter the number of names: "))
names = []

for i in range(n):
    name = input(f"Enter name {i+1}: ").strip()
    names.append(name)

char = input("Enter the character to filter names: ").strip()

print(f"Names starting with '{char}':")
for name in names:
    if name.startswith(char):
        print(name)