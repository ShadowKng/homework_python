from datetime import date
 
def spec(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False
 
print(spec(2022, 24, 23))
print(spec(2021, 4, 9))