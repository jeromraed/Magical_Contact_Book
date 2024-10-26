from MagicalContact import MagicalContact

class MagicalCreature(MagicalContact):
    def __init__(self,name,email,phone_number,species,tamed):
        super().__init__(name,email,phone_number)
        self.__species=species
        if isinstance(tamed,bool):
            self.tameness=tamed
        else: raise ValueError("tameness must be a boolean value.")

    def get_species(self):
        return self.__species

    def is_tame(self):
        if self.tameness:
            print("is tamed")
        else: print("is not tamed")

    def describe(self):
        super().describe()
        print(f"Species:{self.__species}\nTameness:{self.is_tame()}")