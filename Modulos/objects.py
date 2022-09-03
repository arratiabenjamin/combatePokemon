import os

#SKILLS
class Skills():
    def __init__(self, name, element, tipo, power):
        self.name = name
        self.element = element
        self.tipo = tipo
        self.power = power

PunoFuego = Skills('Puño Fuego', 'Fuergo', 'Ataque', 75)
EnviteIgneo = Skills('Envite Igneo', 'Fuego', 'Ataque', 120)
ColmilloIgneo = Skills('Colmillo Igneo', 'Fuego', 'Ataque', 65)
TajoAereo = Skills('Tajo Aereo', 'Volador', 'Ataque', 75)
TajoUmbrio = Skills('Tajo Umbrio', 'Siniestro', 'Ataque', 70)
ShurikenAgua = Skills('Shuriken de Agua', 'Agua', 'Ataque', 75)
PulsoUmbrio = Skills('Pulso Umbrio', 'Siniestro', 'Ataque', 80)
Paranormal = Skills('Paranormal', 'Psiquico', 'Ataque', 80)
PunoTrueno = Skills('Puño Trueno', 'Electrico', 'Ataque', 75)
Impactrueno = Skills('Impactrueno', 'Electrico', 'Ataque', 40)
MegaPuno = Skills('Mega Puño', 'Normal', 'Ataque', 80)
GolpeCuerpo = Skills('Golpe Cuerpo', 'Normal', 'Ataque', 70)
PunoDinamico = Skills('Puño Dinamico', 'Lucha', 'Ataque', 100)
GarraMetal = Skills('Garra Metal', 'Acero', 'Ataque', 50)
CabezazoZen = Skills('Cabezazo Zen', 'Psiquico', 'Ataque', 80)
Terremoto = Skills('Terremoto', 'Tierra', 'Ataque', 100)
GolpeAereo = Skills('Golpe Aereo', 'Volador', 'Ataque', 60)
GarraDragon = Skills('Garra Dragon', 'Dragon', 'Ataque', 80)
GarraUmbria = Skills('Garra Umbria', 'Fantasma', 'Ataque', 70)

Fatallity = Skills('Fatallity', 'Oscuro', 'Ataque', 9892)


#POKEMONS
class Pokemon():
    def __init__(self, name, hp, attack, defense, speed, element, scream, mov1 = 'Vacio', mov2 = 'Vacio', mov3 = 'Vacio', mov4 = 'Vacio' ):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.element = element
        self.scream = scream
        self.mov1 = mov1
        self.mov2 = mov2
        self.mov3 = mov3
        self.mov4 = mov4

#Vida:329
Charizard = Pokemon(
    'Charizard', 
    329, 236, 224, 268, 
    'Fuego/Volador', 
    'GROOAAA!!', 
    PunoFuego, EnviteIgneo, ColmilloIgneo, TajoAereo
    )
#Vida:317
Greninja = Pokemon(
    'Greninja', 
    317, 258, 202, 312,
    'Agua/Siniestro', 
    'Gruuu..', 
    TajoUmbrio, ShurikenAgua, PulsoUmbrio, Paranormal
    )
Pikachu = Pokemon(
    'Pikachu', 
    263, 228, 168, 308, 
    'Electrico', 
    'Pika Piii!!', 
    PunoTrueno, Impactrueno, MegaPuno
    )
Metagross = Pokemon(
    'Metagross', 
    333, 338, 328, 208, 
    'Acero/Psiquico', 
    'Metaaa!!', 
    GolpeCuerpo, PunoDinamico, GarraMetal, CabezazoZen
    )
Haxorus = Pokemon(
    'Haxorus', 
    325, 362, 248, 262, 
    'Dragon', 
    'Gaaaa!!', 
    Terremoto, GolpeAereo, GarraDragon, GarraUmbria
    )

#LISTA CON TODOS LOS POKEMON
pokemons = [Charizard, Greninja, Pikachu, Metagross, Haxorus]


#TRAINERS
class Trainer():
    def __init__(self, name, age, pokemon = None):
        self.name = name
        self.age = age
        self.pokemon = pokemon


while True:
    try:
        trainer1 = Trainer('Benjamin', 17)
        os.system('cls')
    except:
        print('Ingreso erroneamente sus datos vuelva a intentarlo.')
    else:
        print('Todo Correcto espere a que el proximo Trainer ingrese los datos.')
        break

while True:
    try:
        trainer2 = Trainer('Maxi', 32)
        os.system('cls')
    except:
        print('Ingreso erroneamente sus datos vuelva a intentarlo.')
    else:
        print('Todo Correcto\nEmpezara la eleccion de Pokemon.')
        break