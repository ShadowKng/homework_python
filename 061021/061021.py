a = input("Ur name: ")
b = input("Your phone number by example +7-989-xxx-xx-xx: ")
g = {}
while b != "q" and a != "q":
    if len(b) == 16 and b[0] + b[2] + b[6] + b[10] + b[13] == "+----" and (
            b[1] + b[3] + b[4] + b[5] + b[7] + b[8] + b[9] + b[11] + b[12] + b[14] + b[15]).isdigit():
        g[a] = b
        print("Number added")
    else:
        print("Wrong number")
    a = input("Ur name: ")
    b = input("Your phone number by example +7-989-xxx-xx-xx: ")
print(g)