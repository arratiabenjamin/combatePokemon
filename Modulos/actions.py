from random import randint, choices
from Modulos import elections as elects
import time, os

#Generador de formula
def genFormulation(trainerAttacking, trainerAttacked):

    #VARIABLES
    #Pokes
    pokemonAttacking = trainerAttacking.pokemon
    pokemonAttacked = trainerAttacked.pokemon

    #Atks
    atkPokemon = elects.electionAttack(trainerAttacking)
    atkPokemonElement = atkPokemon.element
    atkVeryEffective = atkPokemonElement.veryEffective
    atkIneffectual = atkPokemonElement.ineffectual
    atkNull = atkPokemonElement.null

    #ElementsPokeAttaking
    pokemonAttackingElement1 = pokemonAttacking.element1
    pokemonAttackingElement2 = pokemonAttacking.element2

    #ElementPokeAttacked
    pokemonAttackedElement1 = pokemonAttacked.element1

    #mod1 y mod2 aun no se implementan por completo solo existen para recrear la formula.
    mod1 = 1
    mod2 = 1

    #Stab ElementSkill == ElementsPoke
    stab = 1

    #EffectsElement (Critico-Efectivo-PocoEfectivo-Nulo)
    effectElement1 = 1
    effectElement2 = 1
    
    #ChanceCritico - Random
    CH = choices([1,1.5], weights = (80, 25)) #ListaOriginal = [1,2]
    RND = randint(85, 101)


    #FORMULAS
    formLvl = 1.5 * pokemonAttacking.lvl / 5 + 2 #MultiplicacionOriginal = 2
    formAPD = pokemonAttacking.attack * atkPokemon.power / pokemonAttacked.defense

    #Comprobacion si el elemento del movimiento coincide con alguno del pokemon.
    if atkPokemonElement == pokemonAttackingElement1 or atkPokemonElement == pokemonAttackingElement2:
        stab = 1.5

    #Comprobacion Efectividad de Elemento 1
    if pokemonAttackedElement1.name in atkVeryEffective or 'ALL' in atkVeryEffective:
        effectElement1 = 1.5 #Original = 2
    elif pokemonAttackedElement1.name in atkIneffectual:
        effectElement1 = 0.5
    elif pokemonAttackedElement1.name in atkNull:
        effectElement1 = 0
    

    #FORMULA FINAL
    totalAttack = int( ( ( ( (formLvl * formAPD) / 50 ) * mod1 + 2 ) * stab * effectElement1 * effectElement2 * mod2 * RND/100 ) * CH[0] )

    return totalAttack, CH, effectElement1

#Ataque Pokemon
def attack(trainerAttacking, trainerAttacked):

    print(f'\t\t{trainerAttacking.name} Elije tu ataque.')
    
    #Variable total de ataque - Chance de critico - Effecto del elemento 1
    totalAttack, CH, effectElement1 = genFormulation(trainerAttacking, trainerAttacked)
    
    #Muestra de eficacia
    if effectElement1 == 0:
        print('\t\t\t\t\t El ataque no es eficaz!!')
    elif effectElement1 == 0.5:
        print('\t\t\t\t\t El ataque es poco eficaz!!')
    elif effectElement1 == 1.5:
        print('\t\t\t\t\t El ataque es muy eficaz!!!')
    else:
        print('\t\t\t\t\t El ataque es eficaz!')

    #Muestra si fue critico
    if CH[0] == 1.5:
        print('\t\t\t\t\t El ataque fue CRITICO!!')

    #Resta de ataque total a vida de pokemon atacado
    trainerAttacked.pokemon.hp -= totalAttack

    #Comprobacion por si es que la vida bajo de 0 y solo dejar hasta 0
    if trainerAttacked.pokemon.hp < 0:
        trainerAttacked.pokemon.hp = 0

    print(f'\n\t\t\t\t\t     Vida de {trainerAttacked.pokemon.name} = {trainerAttacked.pokemon.hp}')
    time.sleep(2.5)
    os.system('cls')

    #Comprobacion si murio y muestra de mensaje de quien perdio y quien gano.
    if trainerAttacked.pokemon.hp == 0:
        print('\n\n\n\n\n')
        print('\n\n')
        print('\t\t\t\t     *****************************************************')
        print(f'\n\n\t\t\t\t\t  |{trainerAttacked.name}| A PERDIDO EL COMBATE!!')
        print(f'\n\n\t\t\t\t\t      POR LO QUE |{trainerAttacking.name}| ES EL GANADOR!!\n\n')
        print('\t\t\t\t     *****************************************************')
        time.sleep(3)
    
    return trainerAttacked.pokemon.hp

