import os, time
from Modulos import objects as obj

def electionPokemon(nameTrainer):
    
    os.system('cls')

    trainer = ''
    while trainer == '':

        print('\n\n\n\n\n')
        print('\n\n')
        print('\t\t\t\t     **************************************************')
        print('\t\t\t\t     * SELECCIONE UNO DE ESTOS POKEMONS POR SU NUMERO *')
        print('\t\t\t\t     **************************************************\n')

        for p in obj.pokemons:
            index = obj.pokemons.index(p)
            print(f'\t\t\t\t     {index + 1}.- {p.name}')

        trainer = input(f'\n\n\t\t\t\t     {nameTrainer}: ')
        os.system('cls')
        
        
        print('\n\n\n\n\n')
        print(f'{nameTrainer}:\n')
        if trainer == '':
            print('No ha elegido un pokemon')
            print('Tendra que repetir la eleccion')
        elif int(trainer) - 1 not in range(len(obj.pokemons)):
            print('Su pokemon no fue encontrado')
            print('Tendra que elegir nuevamente')
            trainer = ''
        else:
            print('Su pokemon fue encontrado')
            trainer = int(trainer)
            trainer -= 1
            trainer = obj.pokemons[trainer]
        
    
    os.system('cls')
    return trainer

def electionAttack(trainerPokemon):

    skillsPokeList = [
        trainerPokemon.pokemon.mov1,
        trainerPokemon.pokemon.mov2,
        trainerPokemon.pokemon.mov3,
        trainerPokemon.pokemon.mov4
    ]

    while True:

        os.system('cls')
        
        print('\n\n\n\n\n')
        print(f'\t\t\t\t\t\t  Turno de {trainerPokemon.name}')

        print('\n\n\n\n\n')
        print('\n\t\t\t\t\t     Skills del Pokemon: \n')
        for s in skillsPokeList:
            index = skillsPokeList.index(s)
            if s == 'Vacio':
                print(f'\t\t\t\t\t\t      {index + 1}.- {s}')
            else:
                print(f'\t\t\t\t\t\t      {index + 1}.- {s.name}')

        skillElected = input('\n\t\t\t\t\t     Elija la Skill a usar: ')

        match skillElected:
            case '1': skillElected = skillsPokeList[0]
            case '2': skillElected = skillsPokeList[1]
            case '3': skillElected = skillsPokeList[2]
            case '4': skillElected = skillsPokeList[3]
            case _: skillElected = 'Casilla Inexistente'

        os.system('cls')
        
        print('\n\n\n\n\n')
        print('\n\n\n')
        if skillElected == 'Vacio':
            print('\n\t\t\t\t\t     La casilla escogida esta vacia.')
            print('\t\t\t\t\t     Debera volver a elegir.\n')
            time.sleep(2)
        elif skillElected == 'Casilla Inexistente':
            print('\n\t\t\t\t\t     La casilla no existe.')
            print('\t\t\t\t\t     Debera vovler a elegir.\n')
            time.sleep(2)
        else:
            os.system('cls')
            print('\n\n\n\n\n')
            print('\n\n')
            print('\n\t\t\t\t\t     Skill Encontrado, el pokemon atacara\n')
            return skillElected
            break
