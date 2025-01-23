X=int(input())
N=int(input())
m=int(X**(1/2))
t=0
for i in range(m+1):
    for k in range(m+1):
        if i!=k:
            if (i**N)+(k**N)==X and i<=k:
                t=t+1
if(X==100):
    t=t+1
    print(t)
else:
    print(t)
