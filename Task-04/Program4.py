s=input()
l=[0,0,0,0,0,0,0,0,0,0]
for i in s:
    if i.isdigit():
        l[int(i)]=s.count(i)
for j in l:
    print(j,end=' ')
