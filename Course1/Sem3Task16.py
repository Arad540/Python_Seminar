n = int(input('Put range of the list: '))
data = [int (i) for i in  input ('put list numbers: ').split()]
if len(data) == n:
   x = int (input('Put the number (X) you want to count: '))
   count = 0
   for i in range (n):
     if data[i] == x:
         count +=1
else:
    print('More than N elements of the list')

print(f'Number {x} repeats in the list {count} time(s)')