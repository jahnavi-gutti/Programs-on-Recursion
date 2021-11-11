def print1ton(n):
    if n==0:
        return
    print(n)
    print1ton(n-1)
    
   
n=int(input())
print1ton(n)
