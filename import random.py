import random

def get_names(names, sec_names, surnames, num): 
    result = []
    i = 0
    while i < num:
        new_n = random.choice(names)
        new_sn = random.choice(sec_names)
        new_sur = random.choice(surnames)
        name = new_n + ' ' + new_sn + ' ' + new_sur
        result += name
        i += 1
    return result

n = []
s = []
sur = []
get(n, s, sur, 10)