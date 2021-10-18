from initialz import initials


def initials_list(names_list):
    new_names = []
    for name in names_list:
          new_names.append(initials(name))
    return new_names

print(initials_list(['Aaaaa Bbbb Ccccc', 'Ddddd Eeee Fffff']))