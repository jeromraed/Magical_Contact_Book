from MagicalContact import MagicalContact

class MagicUser(MagicalContact):
    HogwartsHouses=['Gryffindor','Slytherin','Hufflepuff','Ravenclaw']

    def __init__(self,name,email,phone_number,house,core,wood,length):
        super().__init__(name,email,phone_number)
        # while house not in MagicUser.HogwartsHouses:
        #     house=input(f'Invalid House:{house}\nHouse should be one of{MagicUser.HogwartsHouses}\nEnter new house:')
        if house not in MagicUser.HogwartsHouses:
            raise ValueError(f'Invalid house entered\nHouse should be one of{MagicUser.HogwartsHouses}')
        self.__house=house
        self.__wand={
            'core':core,
            'wood':wood,
            'length':length
        }

    def get_wand(self):
        return f"Length:{self.__wand['length']}\"\tWood:{self.__wand['wood']}\tCore:{self.__wand['core']}"

    def get_house(self):
        return self.__house

    def describe(self):
        super().describe()
        print(f"House:{self.__house}\n{self.get_wand()}")
