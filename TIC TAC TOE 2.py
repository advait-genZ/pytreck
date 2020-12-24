print("The game TIC TAC TOE has 9 places in it with a 3*3 row column arrangement. The user will select the ")
l=['','','','','','','','','']
for i in range (0,9):
    n=int(input("Enter the place no. between 1 & 9"))
    if n>9 or n<1:
        print("The no. should be between 1 and 9")
    else:
        l[n]='X'
    if l[i]==l[i+1]:
        l[i+2]='O'
    elif l[i]==l[i+3]:
        l[i+6]='O'
    elif l[i]==l[i+4]:
        if i==4:
            l[0]=='O'
        elif i==
