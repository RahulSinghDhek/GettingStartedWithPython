__author__ = 'rdhek'

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print [row for row in mat]
print [row[1] for row in mat]
print [col for row in mat for col in row]
print [col for row in mat for col in row if col%2]
print [col for row in mat if len(row)== 3 for col in row if col%2]
print [i **3 for i in row[1] for row in mat]