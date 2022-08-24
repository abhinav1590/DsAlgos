def checkPallindrome(sentence):
    counter,arr,lngWord = 0,[],'' 
    print('Pallindrome words are -',end=' ')
    for word in sentence.split():
        if word == word[::-1] and len(word) != 1:
            print(word, end = ' ')
            counter += 1
            arr.append(word)
    lngWord = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > lngWord:
            lngWord = arr[i]
    print(f'Number of pallindrome letters = {counter} \n Largest Pallindrome word is {lngWord}')
        
if __name__ == '__main__' :
    string = input("\n Enter a sentence \n").lower()
    checkPallindrome(string)
    # print(''.join(reversed(string)))
    print(f'Reverse of string is {string[::-1]}')