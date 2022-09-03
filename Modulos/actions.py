from Modulos import elections as elects
import time, os

def attack(trainerAttacking, trainerAttacked):

    print(f'\t\t{trainerAttacking.name} Elije tu ataque.')
    trainerAttackingAtk = elects.electionAttack(trainerAttacking)
    totalAttack = int((((trainerAttackingAtk.power * trainerAttacking.pokemon.attack / trainerAttacked.pokemon.defense) /50) * 1.5 + 2) * 3.5)
    trainerAttacked.pokemon.hp -= totalAttack

    if trainerAttacked.pokemon.hp < 0:
        trainerAttacked.pokemon.hp = 0

    print(f'\n\t\t\t\t\t     Vida de {trainerAttacked.pokemon.name} = {trainerAttacked.pokemon.hp}')
    time.sleep(2.5)
    os.system('cls')

    if trainerAttacked.pokemon.hp == 0:
        print('\n\n\n\n\n')
        print('\n\n')
        print('\t\t\t\t     *****************************************************')
        print(f'\n\n\t\t\t\t\t  |{trainerAttacked.name}| A PERDIDO EL COMBATE!!')
        print(f'\n\n\t\t\t\t\t      POR LO QUE |{trainerAttacking.name}| A GANADO EL COMBATE!!\n\n')
        print('\t\t\t\t     *****************************************************')
        time.sleep(3)
    return trainerAttacked.pokemon.hp