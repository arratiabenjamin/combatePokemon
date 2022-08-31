from Modulos import attack
from Modulos import pokemons as pokes
import os

def app():
    #ELECCION POKEMON
    trainer1 = ''
    trainer2 = ''
    while trainer1 == '' and trainer2 == '':

        #TRAINER 1
        if trainer1 == '':
            print('\n')
            print('\t\t**************************************************')
            print('\t\t* SELECCIONE UNO DE ESTOS POKEMONS POR SU NUMERO *')
            print('\t\t**************************************************\n')

            for p in pokes.pokemonsText:
                index = pokes.pokemonsText.index(p)
                print(f'\t\t{index + 1}.- {p}')

            trainer1 = input('Trainer 1: ')
            os.system('cls')
            
            print('Entrenador 1:\n')
            if int(trainer1) - 1 not in range(len(pokes.pokemonsText)):
                print('Su pokemon no fue encontrado')
                print('Tendra que elegir nuevamente')
                trainer1 = ''
            else:
                print('Su pokemon fue encontrado')
                trainer1 = int(trainer1)
                trainer1 -= 1
                trainer1 = pokes.pokemonsObject[trainer1]

        #TRAINER 2
        if trainer2 == '':
            print('\n')
            print('\t\t**************************************************')
            print('\t\t* SELECCIONE UNO DE ESTOS POKEMONS POR SU NUMERO *')
            print('\t\t**************************************************\n')

            for p in pokes.pokemonsText:
                index = pokes.pokemonsText.index(p)
                print(f'\t\t{index + 1}.- {p}')

            trainer2 = input('Trainer 2: ')
            os.system('cls')

            print('Entrenador 2:\n')
            if int(trainer2) - 1 not in range(len(pokes.pokemonsText)):
                print('Su pokemon no fue encontrado')
                print('Tendra que elegir nuevamente')
                trainer2 = ''
            else:
                print('Su pokemon fue encontrado')
                trainer2 = int(trainer2)
                trainer2 -= 1
                trainer2 = pokes.pokemonsObject[trainer2]


    #COMIENZO COMBATE POKEMON.
    print('\n')
    print('\t\t*********************************')
    print('\t\t* COMIENZA EL COMBATE POKEMON!! *')
    print('\t\t*********************************\n')

    print('\t\t -------------------------------')
    print('\t\t| Jugador 1 saca a: \t        |')
    print(f'\t\t|\t{trainer1.name} - {trainer1.scream}   |')
    print('\t\t -------------------------------\n\n')

    print('\t\t -------------------------------')
    print('\t\t| Jugador 2 saca a: \t        |')
    print(f'\t\t|\t{trainer2.name} - {trainer2.scream}   |')
    print('\t\t -------------------------------\n\n')
    
app()