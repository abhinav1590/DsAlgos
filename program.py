def getval(num1, num2, number):
    store = abs( num1 - num2 )
    if store % number == 0 :
        return True
    else:
        return False

def calculation(array, number):
    counter1, counter2 , copy, length = 0, 0 , [], len(array)

    for i in range(length):
        for j in range(i+1, length):
            if getval(array[i],array[j],number):
                counter1 +=1 
            else:
                copy.append(array[i])
            counter2 +=1 
    
    copy = list(set(copy))
    if counter1 == counter2:
        print(f'The answer is {number}')
    else:
        print(f'The divisble pair of sets are {copy}')

def value():
    N = list(map(int, input('enter your list \n').split()))
    K = int(input('enter a number in a range of 2 to 1000 \t'))
    if True:
        calculation(N,K)

if __name__ == '__main__':
    value()

