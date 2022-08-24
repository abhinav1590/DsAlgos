class something:
    def __init__(self,mobile, email):
        self.mobile = mobile
        self.email = email
    def printing(self):
        print(f'Your email is {self.email}')


class nothing(something):

    def __init__(self,name, age,mobile,address):
        super().__init__(mobile,address)
        self.human = name
        self.age = age
        
    def print(self):
        if self.human.lower() == 'abhinav':
            print(f'hello {self.human}')
            print(f'your number is {self.mobile}')
            super().printing()
        else:
            print(f'You are not the owner of this laptop')

    def calculate(self):
        if len(self.human)>= 10:
            if self.age >= 18:
                array = list(map(int, input('enter an array').split()))
                num = int(input('enter a number to be searched'))
                counter = 0 
                try:
                    for i in range(len(array)):
                        if num is array[i]:
                            counter +=1 
                    print(counter)
                except:
                    print('NUMBER NOT FOUND')

                reverse = array[::-1]
                print(reverse)
                number = list(map( str, map( float ,map(lambda x : x if (x > 3) else x+3 , array))))[::-1]
                print(number)
            else:
                print('You are still not eligible to do this')

a = input('enter your name Mr/Mrs').strip()      
b = int(input('Enter your age Mr/Mrs'))
c=  int(input('enter your mobile number'))
d = input('enter your address').strip()
person = nothing(a,b,c,d)
print(person.print(), person.calculate())