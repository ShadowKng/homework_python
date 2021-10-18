def cregion(names, cities):
    reg = ()
    for name,city in zip(names, cities):
        reg[name] = city
    return reg
