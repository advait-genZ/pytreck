l=['','','','','','','','','']
for i in range (0,9):
    n=int(input("Enter the place no. between 0 & 8"))
    if n>8 or n<0:
        print("The no. should be between 0 and 8")
    else:
        l[n]='X'
    if l[i]==l[i+1]:
        l[i+2]='O'
    elif l[i]==l[i+3]:
        l[i+6]='O'
    elif l[i]==l[i+4]:
        if i==4:
            l[0]=='O' or l[2]=='O'
        elif i==8:
          pass   
if l[i]==l[i+1]==l[i+2] or l[i]==l[i+3]==l[i+6]:
    print("you won")
elif i==0:
    if l[i]==l[i+4]==l[i+8]:
        print("you won")
elif i==2:
    if l[i]==l[i+2]==l[i+4]:
        print("you won")
else:
    print("you lose")
