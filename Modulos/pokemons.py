from Modulos import skills as sk

class Pokemon():
    def __init__(self, name, hp, attack, defense, element, scream, mov1, mov2 = None, mov3 = None, mov4 = None ):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.scream = scream
        self.mov1 = mov1
        self.mov2 = mov2
        self.mov3 = mov3
        self.mov4 = mov4

#POKEMONS
Charizard = Pokemon(
    'Charizard', 
    3592, 400, 142, 
    'Fuego/Volador', 
    'GROOAAA!!', 
    sk.Llamarada, sk.Grunido, sk.CaraSusto
    )
Greninja = Pokemon(
    'Greninja', 
    4872, 473, 93, 
    'Agua', 
    'Gruuu..', 
    sk.PatadaDoble, sk.CaraSusto, sk.ShurikensAgua
    )

#LISTA CON TODOS LOS POKEMON
pokemonsText = ['Charizard', 'Greninja']
pokemonsObject = [Charizard, Greninja]