from Modulos import elections as elects, objects as obj
import time, os


def app():
    try:

        #CREACION DE TRAINER
        trainer1 = obj.trainer1
        trainer2 = obj.trainer2

        #ELECCION POKEMON
        trainer1.pokemon = elects.pokemon(trainer1.name)
        trainer2.pokemon = elects.pokemon(trainer2.name)

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
        
        #ELECCION MOVIMIENTO
        while trainer1.pokemon.hp > 0 and trainer2.pokemon.hp > 0:

            #VERIFICACION DE QUIEN COMENZARA PRIMERO SEGUN VELOCIDAD DE POKEMON
            #DENTRO DEL BUCLE POR EFECTOS DE OBJETOS
            if trainer2.pokemon.speed > trainer1.pokemon.speed:
                #CAMBIO DE LUGARES SI ES QUE POKEMON DE TRAINER2 ES MAS VELOZ
                trainer1, trainer2 = trainer2, trainer1

            elects.movement(trainer1, trainer2)
            if trainer2.pokemon.hp == 0:
                break
            elects.movement(trainer2, trainer1)
        
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
        print('\t\t\tEl juego se cerrara en 3 segundos.')
        time.sleep(3)

app()