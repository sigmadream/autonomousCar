import csv

 
# save data in csv file.

f=open('./data/test.csv','w')
fwriter = csv.writer(f, delimiter=";", lineterminator="\n")

fwriter.writerow((1, 'Hello World!!!'))

f.close()
