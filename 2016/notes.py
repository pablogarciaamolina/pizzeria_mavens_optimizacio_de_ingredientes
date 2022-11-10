import pandas as pd

d0 = pd.to_datetime('18:42 PM')
d1 = pd.to_datetime('15:09:12', dayfirst=True)
d2 = pd.to_datetime('00H 00M 00S', dayfirst=True)
d3 = pd.to_datetime('2016-06-21', dayfirst=True)
d4 = pd.to_datetime('May 29 2016', dayfirst=True)

print(str(d0))
print(d1)
print(d2)
print(d3)
print(d4)