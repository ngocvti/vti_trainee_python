# Table Printer
import numpy as np
table_data = np.array([['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']])
              
table = table_data.transpose()

for i in range(len(table)):
    for j in range(len(table[0])):
        print(table[i][j], end = " ")
    print()