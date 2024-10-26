class MagicalContact:
    def __init__(self,name,email,phoneNumber):
        self.__name=name
        self.__email=email
        self.__phoneNumber=phoneNumber

    def get_name(self):
        return self.__name

    def set_name(self,newname):
        self.__name=newname

    def get_email(self):
        return self.__email

    def set_email(self,newEmail):
        self.__email=newEmail

    def get_phone_number(self):
        return self.__phoneNumber

    def set_phone_number(self,new_phone_number):
        self.__phoneNumber=new_phone_number

    def describe(self):
        print(f'Name:{self.__name}\nEmail:{self.__email}\nPhone Number:{self.__phoneNumber}')
