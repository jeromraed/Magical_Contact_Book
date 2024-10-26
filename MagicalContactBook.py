class MagicalContactBook:
    def __init__(self,contacts):
        self.__contacts=contacts

    def add_contact(self,contact):
        self.__contacts.append(contact)

    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()

    def find_contact(self,name):
        for contact in self.__contacts:
            if contact.get_name()==name:
                return contact.describe()

        print(f'There is no contact named {name}')