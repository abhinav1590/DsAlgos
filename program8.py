# program to print first letter of all words
def firstCharOfWord(string):
    [print( str[0].lower(), end=' ') for str in string.strip().split()]

# program to replace character 
def replaceCharacter(string):
    newString = []
    for i,word in enumerate(string.strip().split()):
        newString.append('*' if char in ['a','e','i','o','u'] else char for char in word) 
    print(''.join(newString[i]), end=' ')

# program to print in triangle form
def trianglePrint(string):
    word = string.strip().split()[0]
    for i in range(len(word)):
        for pos in range(i+1):
            print(word[pos], end='')
        print(' ')

# program to short the name eg- Abhinav Mishra - A.M. and Abx Kxsh Mishra - A.K. Mishra 
def shortner(string):
    name = string.strip().split()
    [print( str[0].upper(),'.',end='') for str in name] 
    print()
    for i,str in enumerate(name): 
        if i< len(name)-1: print(str[0].upper(),'.',end='')
        else: print(str)

if __name__ == '__main__':
    string = input('Enter a sentence/name/word etc')
    val = True
    while val:
        print('what do yo want to do with this sentence ' , end ='')
        choice = int(input())
        if choice == 1: firstCharOfWord(string)
        elif choice == 2: replaceCharacter(string)
        elif choice == 3: trianglePrint(string)
        elif choice == 4: shortner(string)
        if input("\n Do you want to continue Y/N ?") == 'N':
            val = False
