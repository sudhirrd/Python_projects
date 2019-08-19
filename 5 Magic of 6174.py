""" 6174 is "Kaprekar's constant"
    Take a 4 digit number with at least 2 distinct digits,
    order the numbers within it in ascending and descending order,
    subtract the smaller number from the larger,
    and repeat with the result,
    You'll eventually always end up with 6174"""

import pandas as pd

dataframe = pd.DataFrame()
d_n1 = []
d_n2 = []
d_n = []

n = int(input("Enter Number : "))

match = 6174
while(n != match):
    temp = sorted(str(n))

    n1 = int( "".join(temp) )
    temp.reverse()
    n2 = int( "".join(temp) )
    n = n2 - n1

    d_n1.append(n1)
    d_n2.append(n2)
    d_n.append(n)

dataframe["n2"] = d_n2
dataframe["n1"] = d_n1
dataframe["n"] = d_n

print(dataframe)
