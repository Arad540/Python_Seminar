text = input().lower().split()
result = set()
vowels = 'ёуеыаоэяию'
for word in text:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    result.add(count)
    
print(result)
if len(result) == 1:
    print ("Парам пам-пам")
else:
    print("Пам парам")            