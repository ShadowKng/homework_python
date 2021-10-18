def valid_name(name):
        return name[0].isupper() and name[1:].islower()
         
print(valid_name("aaaaa"))