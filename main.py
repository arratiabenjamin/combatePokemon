from Modulos import attack
from Modulos import pokemons as pokes, elections as elects
import os


def app():
    #ELECCION POKEMON
    trainer1 = elects.electionPokemon('Trainer1')
    trainer2 = elects.electionPokemon('Trainer2')

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
    
    elects.electionAttack(trainer1)

app()