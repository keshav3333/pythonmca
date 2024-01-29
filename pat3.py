row = int(input('enter a number of rows:- '))

out='''
'''

for i in range(1,row+1):
    out= out+(' '*(row-i)+'* '*i)
    out=out+'\n'

for i in range(0,row):
    out=out+(' '*(row-i)+'*'*(i*2+1))
    out=out+'\n'

print(out)
# name= input('enter name of the file :- ')
# with open(f'{name}.txt','w') as file:
#     file.write(out)