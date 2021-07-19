import pandas as pd

wb = pd.read_excel('automate_online-materials/censuspopdata.xlsx')

print(wb.head())

colu = wb['County']

for i in colu:
    print(i)






