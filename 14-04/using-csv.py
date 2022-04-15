import csv

'''f = open('pessoas.csv', 'r')
csvreader = csv.reader(f)
for row in csvreader:
   print(row)'''

juliano = ['juliano', 33, 'mt']
jaina = ['jaina', 19, 'ro']
guilherme = ['guilherme', 20, 'ro']
l = [juliano, jaina, guilherme]

f = open('output.csv', 'w')
writer = csv.writer(f)
writer.writerows(l)