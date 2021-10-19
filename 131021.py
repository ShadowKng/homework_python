class Matrix:
 def __init__(self, M):
    self.M = M
    min = len(M[0])
    t = True
    for i in range(len(M)):
        if len(M[i]) != min:
            t = False
    if not t:
        print("...")

 def transpone(self):
    newM = []
    i = 0
    for i in range(len(self.M[i])):
        b = []
        for j in range(len(self.M)):
            b.append(self.M[j][i])
        newM.append(b)
    return newM

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
try:
    print(matrix.transpone())
except:
    print("некорректная матрица")