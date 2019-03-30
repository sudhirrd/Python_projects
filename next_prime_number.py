num=int(input("ENTER NUMBER AFTER WITCH YOU WANT A PRIME NUMBER : "))
def check(n):
    i=2
    while(i<=int(n/2)):
        if(n%i==0):
            return 0
        i+=1
    else:
        return 1
if(check(num)==1):
    num+=1
while(check(num)==0):
    num+=1
print(num)