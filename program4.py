size = int(input('Enter the number of dictionaries inside the list'))
dictList = []

# format of input should be with space and enter 
for i in range(size):
    n = int(input(f'Dictionary- {i} \n enter the number of list').strip()) 
    print('enter key and value with space only')
    d=dict(input().strip().split() for _ in range(n))
    dictList.append(d)

#format should be space only 
keys = tuple(input('Enter special keys').strip().split())
print(dictList)

specialValues = ''
values = ''
result = []
for DictValue in dictList:
    for k,v in DictValue.items():
        count = 0
        for key in keys:
            if k == key:
                specialValues += v
                count += 1
        if count != 1:
            values += v
    
    x = [digit for digit in values]
    y = [digit for digit in specialValues]
    result.append(f'{"".join(sorted(y))}{"".join(sorted(x))}')

print(result)