import os
import time

#ELEMENTS
class Element():
    def __init__(self, name, veryEffective, ineffectual = [], null = ['Ninguno']):
        self.name = name
        self.veryEffective = veryEffective
        self.ineffectual = ineffectual
        self.null = null

Normal = Element(
    'Normal',
    [],
    ['Roca', 'Acero'],
    ['Fantasma']
    )
Lucha = Element('Lucha',
    ['Normal', 'Roca', 'Hielo', 'Siniestro'],
    ['Volador', 'Veneno', 'Bicho', 'Psiquico', 'Hada'],
    ['Fantasma']
    )
Volador = Element('Volador',
    ['Lucha', 'Bicho', 'Planta'],
    ['Roca', 'Acero', 'Electrico'],
    )
Veneno = Element('Lucha',
    ['Planta', 'Hada'],
    ['Veneno', 'Tierra', 'Roca', 'Fantasma'],
    ['Acero']
    )
Tierra = Element('Tierra',
    ['Veneno', 'Acero', 'Fuego', 'Electrico'],
    ['Bicho', 'Planta'],
    ['Volador']
    )
Roca = Element('Roca',
    ['Volador', 'Bicho', 'Fuego', 'Hielo'],
    ['Lucha', 'Tierra', 'Acero']
    )
Bicho = Element('Bicho',
    ['Planta', 'Psiquico', 'Siniestro'],
    ['Lucha', 'Volador', 'Veneno', 'Fantasma', 'Acero', 'Fuego', 'Hada']
    )
Fantasma = Element('Fantasma',
    ['Fantasma', 'Psiquico'],
    ['Siniestro'],
    ['Normal']
    )
Acero = Element('Acero',
    ['Roca', 'Hielo', 'Hada'],
    ['Acero', 'Fuego', 'Agua', 'Electrico']
    )
Fuego = Element('Fuego',
    ['Bicho', 'Acero', 'Planta', 'Hielo'],
    ['Roca', 'Fuego', 'Agua', 'Dragon']
    )
Agua = Element('Agua',
    ['Tierra', 'Roca', 'Fuego'],
    ['Agua', 'Planta', 'Dragon']
    )
Planta = Element('Planta',
    ['Tierra', 'Roca', 'Agua'],
    ['Volador', 'Veneno', 'Bicho', 'Acero', 'Fuego', 'Planta', 'Dragon']
    )
Electrico = Element('Electrico',
    ['Volador', 'Agua'],
    ['Planta', 'Electrico', 'Dragon'],
    ['Tierra']
    )
Psiquico = Element('Psiquico',
    ['Lucha', 'Veneno'],
    ['Acero', 'Psiquico'],
    ['Siniestro']
    )
Hielo = Element('Hielo',
    ['Volador', 'Tierra', 'Planta', 'Dragon'],
    ['Acero', 'Fuego', 'Agua', 'Hielo']
    )
Dragon = Element('Dragon',
    ['Dragon'],
    ['Acero'],
    ['Hada']
    )
Siniestro = Element('Siniestro',
    ['Fantasma', 'Psiquico'],
    ['Lucha', 'Siniestro', 'Hada']
    )
Hada = Element('Hada',
    ['Lucha', 'Dragon', 'Siniestro'],
    ['Veneno', 'Acero', 'Fuego']
    )

#ElementPokemonJefe
Demoniaco = Element('Demoniaco',
    ['ALL']
    )


#SKILLS
class Skill():
    def __init__(self, name, element, tipo, power):
        self.name = name
        self.element = element
        self.tipo = tipo
        self.power = power

#Todos los poderes originales de las skills son 20 mas (Excluyendo a los que se especifica)
PunoFuego = Skill('Puño Fuego', Fuego, 'Ataque', 55)
EnviteIgneo = Skill('Envite Igneo', Fuego, 'Ataque', 80) #PowerOriginal: 120
ColmilloIgneo = Skill('Colmillo Igneo', Fuego, 'Ataque', 45)
TajoAereo = Skill('Tajo Aereo', Volador, 'Ataque', 55)
TajoUmbrio = Skill('Tajo Umbrio', Siniestro, 'Ataque', 50)
ShurikenAgua = Skill('Shuriken de Agua', Agua, 'Ataque', 50) #PowerOriginal: 15 por Shuriken (5 max)
PulsoUmbrio = Skill('Pulso Umbrio', Siniestro, 'Ataque', 60)
Paranormal = Skill('Paranormal', Psiquico, 'Ataque', 60)
PunoTrueno = Skill('Puño Trueno', Electrico, 'Ataque', 55)
Impactrueno = Skill('Impactrueno', Electrico, 'Ataque', 30) #PowerOriginal: 40
MegaPuno = Skill('Mega Puño', Normal, 'Ataque', 60)
GolpeCuerpo = Skill('Golpe Cuerpo', Normal, 'Ataque', 50)
PunoDinamico = Skill('Puño Dinamico', Lucha, 'Ataque', 80)
GarraMetal = Skill('Garra Metal', Acero, 'Ataque', 40)  #PowerOriginal: 50
CabezazoZen = Skill('Cabezazo Zen', Psiquico, 'Ataque', 60)
Terremoto = Skill('Terremoto', Tierra, 'Ataque', 80)
GolpeAereo = Skill('Golpe Aereo', Volador, 'Ataque', 40)
GarraDragon = Skill('Garra Dragon', Dragon, 'Ataque', 60)
GarraUmbria = Skill('Garra Umbria', Fantasma, 'Ataque', 50)

#SkillsPokemonJefe
Fatallity = Skill('Fatallity', Demoniaco, 'Ataque', 10000)
MilCuchillas = Skill('Mil Cuchillas', Demoniaco, 'Ataque', 10000)
Guadaña = Skill('Guadaña', Demoniaco, 'Ataque', 10000)
EjercitoEsqueletos = Skill('Ejercito de Esqueletos', Demoniaco, 'Ataque', 10000)


#POKEMONS
class Pokemon():
    def __init__(self, name, lvl, hp, attack, defense, speed, element1, element2, scream, mov1 = 'Vacio', mov2 = 'Vacio', mov3 = 'Vacio', mov4 = 'Vacio' ):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.element1 = element1
        self.element2 = element2
        self.scream = scream
        self.mov1 = mov1
        self.mov2 = mov2
        self.mov3 = mov3
        self.mov4 = mov4

#Todos los hp originales son 200 menos
Charizard = Pokemon(
    'Charizard', 100,
    529, 236, 224, 268, 
    Fuego, Volador, 
    'GROOAAA!!', 
    PunoFuego, EnviteIgneo, ColmilloIgneo, TajoAereo
    )
Greninja = Pokemon(
    'Greninja', 100,
    517, 258, 202, 312,
    Agua, Siniestro, 
    'Gruuu..', 
    TajoUmbrio, ShurikenAgua, PulsoUmbrio, Paranormal
    )
Pikachu = Pokemon(
    'Pikachu', 100,
    463, 228, 168, 308, 
    Electrico, 'Ninguno', 
    'Pika Piii!!', 
    PunoTrueno, Impactrueno, MegaPuno
    )
Metagross = Pokemon(
    'Metagross', 100,
    533, 338, 328, 208, 
    Acero, Psiquico, 
    'Metaaa!!', 
    GolpeCuerpo, PunoDinamico, GarraMetal, CabezazoZen
    )
Haxorus = Pokemon(
    'Haxorus', 100,
    525, 362, 248, 262, 
    Dragon, 'Ninguno', 
    'Gaaaa!!', 
    Terremoto, GolpeAereo, GarraDragon, GarraUmbria
    )

#PokemonJefe
Demu = Pokemon(
    'Demu', 100,
    1000, 1000, 1000, 1000, 
    Demoniaco, 'Ninguno', 
    'HHHHH!!!',
    Fatallity, MilCuchillas, Guadaña, EjercitoEsqueletos
    )

#LISTA CON TODOS LOS POKEMON
pokemons = [
    Charizard,
    Greninja,
    Pikachu,
    Metagross,
    Haxorus,
    Demu
    ]


#TRAINERS
class Trainer():
    def __init__(self, name, pokemon = None):
        self.name = name
        self.pokemon = pokemon

#Trainer 1
print('\n\n\n\n\n')
print('\t\t\t\t\t************************************')
print('\t\t\t\t\t* BIENVENIDOS AL COMBATE POKEMON!! *')
print('\t\t\t\t\t************************************\n')
time.sleep(3)

while True:
    try:
        print('\n\n\t\t\t\t\t\t Trainer 1')
        trainer1 = Trainer(input('\n\t\t\t\t\t     Ingrese su nombre: '))
        if trainer1.name == '':
            raise
        os.system('cls')
    except:
        print('\n\t\t\t\tIngreso erroneamente sus datos vuelva a intentarlo.')
        time.sleep(3)
    else:
        print('\n\t\t\t\tTodo Correcto espere a que el proximo Trainer ingrese los datos.')
        time.sleep(3)
        break

#Trainer 2
while True:
    try:
        os.system('cls')
        print('\n\n\t\t\t\t\t\t Trainer 2')
        trainer2 = Trainer(input('\n\t\t\t\t\t     Ingrese su nombre: '))
        if trainer2.name == '':
            raise
    except:
        print('\n\t\t\t\tIngreso erroneamente sus datos vuelva a intentarlo.')
        time.sleep(3)
    else:
        print('\n\t\t\t\t\t\tTodo Correcto\n\t\t\t\t\tEmpezara la eleccion de Pokemon.')
        time.sleep(3)
        break