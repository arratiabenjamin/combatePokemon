import os
from Modulos import pokemons as pokes

def electionPokemon(nameTrainer):
    trainer = ''
    while trainer == '':

        print('\n')
        print('\t\t**************************************************')
        print('\t\t* SELECCIONE UNO DE ESTOS POKEMONS POR SU NUMERO *')
        print('\t\t**************************************************\n')

        for p in pokes.pokemonsText:
            index = pokes.pokemonsText.index(p)
            print(f'\t\t{index + 1}.- {p}')

        trainer = input(f'{nameTrainer}: ')
        os.system('cls')
            
        print(f'{nameTrainer}:\n')
        if trainer == '':
            print('No ha elegido un pokemon')
            print('Tendra que repetir la eleccion')
        elif int(trainer) - 1 not in range(len(pokes.pokemonsText)):
            print('Su pokemon no fue encontrado')
            print('Tendra que elegir nuevamente')
            trainer = ''
        else:
            print('Su pokemon fue encontrado')
            trainer = int(trainer)
            trainer -= 1
            trainer = pokes.pokemonsObject[trainer]
        
    
    os.system('cls')
    return trainer

def electionAttack(skillsPokemon):

    skillsPokeList = [
        skillsPokemon.mov1,
        skillsPokemon.mov2,
        skillsPokemon.mov3,
        skillsPokemon.mov4
    ]

    while True:
        print('Skills del Pokemon: \n')
        for s in skillsPokeList:
            index = skillsPokeList.index(s)
            if s == 'Vacio':
                print(f'\t\t{index + 1}.- {s}')
            else:
                print(f'\t\t{index + 1}.- {s.name}')

        skillElected = input('\nElija la Skill a usar: ')

        match skillElected:
            case '1': skillElected = skillsPokemon.mov1
            case '2': skillElected = skillsPokemon.mov2
            case '3': skillElected = skillsPokemon.mov3
            case '4': skillElected = skillsPokemon.mov4
            case _: skillElected = 'Casilla Inexistente'

        os.system('cls')

        if skillElected == 'Vacio':
            print('\nLa casilla escogida esta vacia.')
            print('Debera volver a elegir.\n')
        elif skillElected == 'Casilla Inexistente':
            print('\nLa casilla no existe.')
            print('Debera vovler a elegir.\n')
        else:
            print('\nSkill Encontrado, el pokemon atacara\n')
            break
