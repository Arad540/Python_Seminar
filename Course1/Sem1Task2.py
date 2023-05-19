n = input('Put your numbner: ')
n = int(n)


if n >= 100 and n<1000:
     d1 = n % 10
     d2 = n % 100 // 10
     d3 = n // 100
     print (d1, ' + ' ,d2,' + ',d3, ' = ', d1+d2+d3)
    
else :

    print ('Number is more than three digits, sorry I cant handle it :( ')
  




