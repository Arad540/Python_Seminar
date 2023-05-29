n = int(input('Put range of the list: '))
data = [int (i) for i in  input ('put list numbers: ').split()]

x = int (input('Put the number (X) you want to check: '))
   
min = abs(x- data[0])

index=0

for i in range (1,n):
    count = abs(x- data[i])
    if count < min:
         min = count
         index = i
         
print(f'number {x} is more near {data[index]} in the list')



        