n=int(input("Enter no of lines upto which the pattern must continue"))
b=1
c=1
for i in range(n):
    d=""
    e=b
    for j in range(b*2-1):
        d+=str(e)
        e+=c
        if e==b*2-1:
            c=-1
        if j==b*2-2:
            c=1
    b+=1
    print(d)
