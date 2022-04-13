class FamilyMember:
    last_name = "Lee"

    def __init__(self,name='NoName',age=0):
        self.name,self.age = name,age

    @classmethod
    def age(cls,age=0):
        return cls('noname',age)

    @staticmethod
    def help():
        print(f"This is FamilyMember Class with last name{FamilyMember.last_name}.")
    @classmethod
    def name(cls,name='noname'):
        return cls(name,0)

    def introduce(self):
        print(f'My name is {self.name} {FamilyMember.last_name},and i am {self.age} years old')

    def identify(self):
        if self.age>=10:
            print("I am adult")
        else:
            print("I am child")
    def introduce_in_korean(self):
        print(f"나의 이름은 {FamilyMember.last_name} {self.name} 제 나이는 {self.age} 입니다")
    @classmethod
    def change_last_name(cls,new_last_name):
        cls.last_name = new_last_name
a= FamilyMember("Hanbit",24)
a.introduce()