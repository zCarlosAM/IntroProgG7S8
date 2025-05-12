print("."*10)

i = 1
j = 1

while i < 6:
    while j < 11:
        print(i, "x", j, "=", i * j)
        j += 1
    print("."*10)
    j = 0
    i += 1