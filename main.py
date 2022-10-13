from Modulos import elections as elects, objects as obj, actions as acts
import time, os

def app():

    os.system('cls')
    try:

        #CREACION DE TRAINER
        trainer1 = obj.trainer1
        trainer2 = obj.trainer2

        #ELECCION POKEMON
        trainer1.pokemon = elects.electionPokemon(trainer1.name)
        trainer2.pokemon = elects.electionPokemon(trainer2.name)

        #AVISO COMIEZO COMBATE Y MUESTRA DE ELECCION POKEMON.
        print('\n\n\n\n\n')
        print('\t\t\t\t\t   *********************************')
        print('\t\t\t\t\t   * COMIENZA EL COMBATE POKEMON!! *')
        print('\t\t\t\t\t   *********************************\n')

        print('\t\t\t\t\t --------------------------------------')
        print(f'\t\t\t\t\t\t {trainer1.name} saca a:')
        print(f'\t\t\t\t\t\t {trainer1.pokemon.name} - {trainer1.pokemon.scream}')
        print('\t\t\t\t\t --------------------------------------\n\n')

        print('\t\t\t\t\t --------------------------------------')
        print(f'\t\t\t\t\t\t {trainer2.name} saca a:')
        print(f'\t\t\t\t\t\t {trainer2.pokemon.name} - {trainer2.pokemon.scream}')
        print('\t\t\t\t\t --------------------------------------\n\n')

        #TIMELAPSE 3S 
        time.sleep(3)
        os.system('cls')

        #VERIFICACION DE QUIEN ATACARA PRIMERO SEGUN VELOCIDAD DE POKEMON
        if trainer2.pokemon.speed > trainer1.pokemon.speed:
            #CAMBIO DE LUGARES SI ES QUE POKEMON DE TRAINER2 ES MAS VELOZ
            trainer1, trainer2 = trainer2, trainer1
        
        #ELECCION ATAQUES Y BUCLE DE COMBATE
        while trainer1.pokemon.hp > 0 and trainer2.pokemon.hp > 0:
            trainer2.pokemon.hp = acts.attack(trainer1, trainer2)
            if trainer2.pokemon.hp == 0:
                break
            trainer1.pokemon.hp = acts.attack(trainer2, trainer1)
        
        #DESPEDIDA
        time.sleep(3)
        os.system('cls')
        print('\n\n\n\n\n')
        print('\n\n\n\n\n')
        print('\t\t\tMuchas gracias por probar mi Combate Pokemon :D')
        
    #Excepcion de interrupcion de tecla por ejemplo: ctrl+z
    except KeyboardInterrupt:
        time.sleep(1)
        os.system('cls')
        print('\n\n\n\n\n')
        print('\n\n\n\n\n')
        print('\t\t\tMuchas gracias por probar mi Combate Pokemon.')
        print('\t\t\tPerdona si no fue tan divertido como para quedarte mas tiempo.')
        
    finally:    
        print('\t\t\tEl juego se cerrara en 7 segundos.')
        time.sleep(7)

app()