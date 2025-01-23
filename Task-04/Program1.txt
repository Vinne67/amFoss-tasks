n=int(input())
l1=list(map(int, input().split()))
m=int(input())
l2=list(map(int, input().split()))
for i in l2:
    for j in l1:
        if (i==j):
            l2.remove(i)
            l1.remove(j)
l2.sort()
l2=set(l2)
for k in l2:
    print(k, end=" ")
