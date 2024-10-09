def nth_fibonacci_number(n):
    if n==0:
        return 0
    if n==1:
        return 1

    F= [None] * (n+1)
    F[0]=0
    F[1]=1

    for i in range(2, n+1):
        F[i] = F[i-1]+ F[i-2]

    return F[n]
n=7
print(f"{n}th fibonacci number is :", nth_fibonacci_number(n))