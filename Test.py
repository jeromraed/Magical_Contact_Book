from MagicUser import MagicUser
from MagicalContactBook import MagicalContactBook

Harry=MagicUser('Harry potter','harrypotter@hogwarts.mom','there was no phones in Harry Potter ya 3m Pola','Gryffindor','Phoenix feather','Holly',11)

# Harry.describe()
Hermione=MagicUser('Hermione Granger','HermionelovesRon@hogwarts.mom','hya muggle bs m3rfsh kan 3ndohom phones wla la','Gryffindor','Dragon heartstring','vine',10.75)

my_book=MagicalContactBook([Harry])
my_book.list_contacts()
print()
my_book.add_contact(Hermione)
my_book.list_contacts()
print()
my_book.find_contact('Hermione Granger')
print()
my_book.find_contact('Hermione')
