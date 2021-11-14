# 1+ 1/3 + 1/9 + 1/27 + … + 1/(3^n) 
def sum(n):
    if n == 0:
        return 1
    return 1 / pow(3, n) + sum(n-1)
n = 5
print(sum(n))
