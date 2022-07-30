# recursive function for fibonacci series

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

x=1
while x<=10:
    print(fibo(x))
    x=x+1
else:
    print("DONE")

