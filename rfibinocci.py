n=int(input())
def fib(n):
    if n==1 or n==2:
        return 1
    f1=fib(n-1)
    f2=fib(n-2)
    oup=f1+f2
    return oup
print(fib(n))
