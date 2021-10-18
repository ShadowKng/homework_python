def initials(name):
    wl = name.split()
    new_name = wl[0]+ '.' + wl[1][0]+ '.' + wl[2][0]+ '.'
    return new_name

print(initials("Aaaa Bbbb Cccc"))