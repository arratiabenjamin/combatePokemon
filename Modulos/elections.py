import os, time
from Modulos import objects as obj, actions as acts


#Eleccion de Pokemon
def pokemon(nameTrainer):
    
    os.system('cls')

    trainer = ''

    #Bucle hasta que se elijan los pokemons
    while trainer == '':

        print('\n\n\n\n\n')
        print('\n\n')
        print('\t\t\t\t     **************************************************')
        print('\t\t\t\t     * SELECCIONE UNO DE ESTOS POKEMONS POR SU NUMERO *')
        print('\t\t\t\t     **************************************************\n')

        #Iteracion para mostrar cada pokemon
        for p in obj.pokemons:
            index = obj.pokemons.index(p)
            print(f'\t\t\t\t     {index + 1}.- {p.name}')

        trainer = input(f'\n\n\t\t\t\t     {nameTrainer}: ')
        os.system('cls')
        
        
        print('\n\n\n\n\n')
        print(f'{nameTrainer}:\n')

        #Comprobacion de eleccion
        if trainer == '':
            print('No ha elegido un pokemon')
            print('Tendra que repetir la eleccion')
        elif not trainer.isnumeric():
            print('Introdujo una cadena de texto.')
            print('Debe introducir el numero del Pokemon.')
            trainer = ''
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

#Eleccion de Ataque
def attack(trainerDuty, trainerWaiting):

    #Lista con skills pokemon atacante
    skillsPoke = [
        trainerDuty.pokemon.mov1,
        trainerDuty.pokemon.mov2,
        trainerDuty.pokemon.mov3,
        trainerDuty.pokemon.mov4
    ]

    #Asignacion variables a pokemons
    pokemonD = trainerDuty.pokemon
    pokemonW = trainerWaiting.pokemon

    #Bucle de eleccion de ataque
    while True:

        os.system('cls')
        
        print('\n\n\n\n\n')
        print(f'\n\t\t\t\t\t     Vida {pokemonD.name}: {pokemonD.hp}')
        print(f'\n\t\t\t\t\t     Vida {pokemonW.name}: {pokemonW.hp} \n\n')
        print('\n\t\t\t\t\t     Skills del Pokemon: \n')

        #Iteracion para muestra de skills
        for s in skillsPoke:
            index = skillsPoke.index(s)
            if s == 'Vacio':
                print(f'\t\t\t\t\t\t      {index + 1}.- {s}')
            else:
                print(f'\t\t\t\t\t\t      {index + 1}.- {s.name}')
        
        print(f'\t\t\t\t\t\t      {index + 2}.- Volver al Menu') #Opicion para volver al menu de eleccion.

        skillElected = input('\n\t\t\t\t\t     Elija su Movimiento: ')

        #Segun la eleccion el valor dado a skillElected
        match skillElected:
            case '1': skillElected = skillsPoke[0]
            case '2': skillElected = skillsPoke[1]
            case '3': skillElected = skillsPoke[2]
            case '4': skillElected = skillsPoke[3]
            case '5': return 'Volver al Menu'
            case _: skillElected = 'Casilla Inexistente'

        os.system('cls')
        
        print('\n\n\n\n\n')
        print('\n\n\n')
        
        #Mensaje para cada tipo de eleccion
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

#Eleccion de Pocion
def objects(trainerDuty, trainerWaiting):

    objectsList = list(trainerDuty.objects) #Lista de Objetos
    
    #Asignacion variables a pokemons
    pokemonD = trainerDuty.pokemon
    pokemonW = trainerWaiting.pokemon

    while True:

        os.system('cls')

        print('\n\n\n\n\n')
        print(f'\n\t\t\t\t\t     Vida {pokemonD.name}: {pokemonD.hp}')
        print(f'\n\t\t\t\t\t     Vida {pokemonW.name}: {pokemonW.hp} \n\n')
        print('\t\t\t\t\t  Sus Pociones son las siguientes: \n')

        #Iteracion para mostrar objetos
        for object, amount in trainerDuty.objects.items():
            index = objectsList.index(object)
            print(f'\t\t\t\t\t\t  {index + 1}.- {object.name} - Tiene {amount}')
        print(f'\t\t\t\t\t\t  {index + 2}.- Volver al Menu\n\n') #Opcion Volver al Menu de eleccion.
        
        electionTrainer = input('\t\t\t\t\t  Elija una de las Opciones(Por su Numero): ')

        #Condicional para saber se introdujo un numero.
        if electionTrainer.isnumeric():
            electionTrainer = int(electionTrainer)

            #Verificacion si eligio Volver al Menu.
            if electionTrainer == index + 2:
                movement(trainerDuty, trainerWaiting)
                break
            
            #Si eligio algun objeto.
            elif electionTrainer > 0 and electionTrainer <= len(objectsList):
                
                #Variable igual al objeto elegido.
                electionTrainer = objectsList[electionTrainer - 1]

                #Si el objeto es sanador y el pokemon tiene la vida al maximo, no sanará.
                if electionTrainer.type == 'Sanador' and trainerDuty.pokemon.hp == trainerDuty.pokemon.hpMax:
                    print('\n\t\t\t\t\t  Su pokemon tiene la vida al Maximo, No puede sanarlo.')
                    print('\t\t\t\t\t  Vuelva a elegir.')
                    time.sleep(2)

                #Si no pasa lo anterior se le aplicara el objeto.
                else:
                    print('\n\t\t\t\t\t  Eligio correctamente. Se le aplicara el efecto a su pokemon.')
                    trainerDuty.objects[electionTrainer] -= 1
                    time.sleep(2)
                    acts.effectPotion(trainerDuty.pokemon, electionTrainer)
                    break

            #Si no eligio un objeto existente.
            else:
                print('\n\t\t\t\t\t  Eligio una Casilla Inexistente.')
                print('\t\t\t\t\t  Vuelva a intentarlo.')
                time.sleep(2)

        #Si no introdujo un numero.
        else: 
            print('\n\t\t\t\t\t  Eligio Erroneamente.')
            print('\t\t\t\t\t  Vuelva a intentarlo.')
            time.sleep(2)

#Eleccion de Movimiento
def movement(trainerDuty, trainerWaiting):

    #Asignacion variables a pokemons
    pokemonD = trainerDuty.pokemon
    pokemonW = trainerWaiting.pokemon

    while True:
        os.system('cls')
        print('\n\n\n\n\n')
        #Muestra de opciones.
        print(f'\n\t\t\t\t\t     Vida {pokemonD.name}: {pokemonD.hp}')
        print(f'\n\t\t\t\t\t     Vida {pokemonW.name}: {pokemonW.hp} \n\n')
        print(f'\t\t\t\t\t\t\t   Entrenador {trainerDuty.name}')
        print('\n\t\t\t\t\t  Elija entre las opciones escribiendo su numero:\n')
        print('\t\t\t\t\t  1.- Ataque Pokemon')
        print('\t\t\t\t\t  2.- Objetos\n')

        electionTrainer = input('\t\t\t\t\t  Introduzca su decision: ')
        
        if electionTrainer == '1': 
            result = acts.attack(trainerDuty, trainerWaiting) #Almacenar resultado por si elige Volver al Menu
            #Si el valor de result es distinto a Volver al Menu se le aplicara a la vida del pokemon enemigo.
            if result != 'Volver al Menu':
                trainerWaiting.pokemon.hp = result
                break
        elif electionTrainer == '2':
            objects(trainerDuty, trainerWaiting)
            break
        else:
            print('\n\t\t\t\t\t Eligio una opcion inexistente.')
            print('\t\t\t\t\t  Vuelva a intentarlo.')
            time.sleep(2)


