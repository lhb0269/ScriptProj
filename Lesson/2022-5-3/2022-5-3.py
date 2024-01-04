import csv

file_nane = 'oscar_age_female.csv'

with open(file_nane,newline="")as f:
    reader = csv.reader(f,skipinitialspace = True)
    for line in reader:
        print(line)

with open(file_nane,newline="")as f:
    reader = csv.DictReader(f,skipinitialspace = True)
    for line in reader:
        print(line['Year'],line['Name'])


#writing

wf = open('converted.scv','w',newline='')
#writer = csv.writer(wf,delimiter = ':',quotechar = "'",quoting=csv.QUOTE_ALL)
writer = csv.DictWriter(wf,fieldnames=['kor','eng','math'],delimiter = ',',quotechar = "'",quoting=csv.QUOTE_ALL)
writer.writerow({'kor':100,'eng':80,'math':100})
writer.writerow({'kor':70,'eng':8,'math':10})
wf.close()