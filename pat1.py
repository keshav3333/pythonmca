rows=int(input('no of rows:- '))
col =int(input('no of cols:- '))
a= rows//2
for i in range(rows):
    for j in range(col):
        
        if i == 0 or i==rows-1:
            print('*',end=' ')
        
        else:
            if j==0 or j == col-1:
                print('*',end = ' ')

            elif j==a-i or j==a+i or i == a+j//2 or i == a-j//2 :
                print('*',end = ' ')
            
             
            else:
                print(' ',end=' ')
            
    print()
