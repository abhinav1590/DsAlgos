class citizen:
    def __init__(self,name, age , email,company):
        self.name = name 
        self.age = age
        self.email = email
        self.company = company

    def check(self):
        if self.age >= 18:
            return True

class company(citizen):

    def __init__(self,name, age , email, Cname):
        super().__init__(name, age , email, Cname)

    def companyCheck(self):
        companies = ['company1',' company2','company3','company4','company5']
        if super().check():
            if companies.index(self.company.lower()):    
                print(f'The company named {self.company.lower()} is present')
            else:
                print('Entered company not found in the list')
        else:
            print("You are not eligible to own a company right now")
    
name = input('Enter your name ').strip()
age = int(input('Enter your age'))
email = input('Enter your email').strip()
Cname = input('Enter your company name').strip()

companyName = company(name,age,email,Cname)
companyName.companyCheck()
