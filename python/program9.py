k = int(input('enter a number'))
List = list(map(int, input('enter a list').split()))
newList = []
for count,i in enumerate(List):
    counter = 0
    num = i 
    print(List[count::])
    for j in List[count:]:
        if num == j:
            counter += 1
    if num in newList:
        pass
    elif counter >= k:
        newList.append(num)
         
print(newList)    