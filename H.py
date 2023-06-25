things = ["everywhere door", "real 3d glasses", "appartment tree"]

print("Put the things in Doraemon's Pocket")
x = str(input(""))

while (x != "finish"):
    things.append(x)
    x = str(input(""))

print("Let see the things inside....")
for i in things:
    print("- " + i)