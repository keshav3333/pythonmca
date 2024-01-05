import csv
# with open('mca.csv','w',newline='') as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id','name','mobile','email'])
#     data1 =[
#         [1,'venu',9078563421,'v@gmail.com'],
#         [2,'abhi',9900768923,'A@gmail.com'],
#         [3,'s@gmail.com',8609609512,'shivu'],
#     ]
#     data.writerows(data1)

# with open('mca.csv','r') as csvfile:
#     data = csv.reader(csvfile)
#     for i in data:
#         print(i)

with open('mca1.csv','w',newline='') as csvfile:
    fieldnames =['id','name','mobile','email']
    data=csv.DictWriter(csvfile,fieldnames)
    data.writeheader()
    rows=[
        {'id':1,'name':'lijitha','mobile':9078190234,'email':'l@gmail.com'},
        {'name':'gurushiva','id':2,'email':'g@gamil.com','mobile':7689051243},


    ]
    data.writerows(rows)
with open('mca1.csv','r') as csvfile:
   
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])

