n = int(input('Put the number of your ticket: '))


if n >= 100000 and n<999999:
     d1 = n // 1000
     a1 = d1 % 10
     a2 = d1 % 100 // 10
     a3 = d1 // 100
     d2 = n % 1000
     b1 = d2 % 10
     b2 = d2 % 100 // 10
     b3 = d2 // 100
     if (a1+a2+a3) == (b1+b2+b3):
         print('Lucky ticket ')
     else: 
         print('No luck')
         
else:
    print ('Number should contain six digits')
    
          
     
     