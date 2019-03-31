num=int(input("ENTER NUMBER FOR WITCH YOU WANT TO FIBONACCI SERIES : "))
i,j=1,1
while(i<=num):
    print(i, ",", j, end=" ,")
    i+=j
    j+=i