n = int(input('Put the first number of your choclate: '))
m = int(input('Put the second number of your choclate: '))
k = int(input('How many pieces of choclate: '))

if n<m:
    if k==n*n:
        print('yes')
    else:
        print ('No')    

else:
    if k==m*m:
        print('yes')
    else:
        print ('No') 
    