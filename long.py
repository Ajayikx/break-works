from Cython.Compiler.Naming import self_cname


class person():
    def __init__(self):
        self.name= ""
        self.tribe= ""

    def get_name(self):
        self.name=input("what is your name sir?: ")
        info = f"welcome Mr {self.name}"
        return info

    def lang(self):
        self.tribe =input("which tribe do you belong: ")
        info2 = f"you are welcome as a {self.tribe} man"
        return  info2


class special_person(person):
    def coding(self):
        he_can_code=input("can you code?: ")
        if he_can_code=='yes':
            print(f"Mr {self_cname} you are welcome" )
        else :
            print ("we are so sorry mr man")
        return


person1=person()
print(person1.get_name())
print(person1.lang())



bob = special_person()
bob.coding()
bob.name