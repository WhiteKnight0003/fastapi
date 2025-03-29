from Enemy import *
from Zombie import *
from Orge import *
from Hero import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
   
    while e1.get_health_points() > 0 and e2.get_health_points() > 0:
        print('------')
        e1.special_attack()
        e2.special_attack()

        print(f'{e1.get_type_of_enemy()} has {e1.get_health_points()} HP')
        print(f'{e2.get_type_of_enemy()} has {e2.get_health_points()} HP')

        e2.attack()
        a1 = e1.get_health_points() - e2.get_attack_damage() 
        e1.set_health_points(a1) 
        
        e1.attack()
        a2 = e2.get_health_points() - e1.get_attack_damage() 
        e2.set_health_points(a2) 

        print('---------')
        print('')
        

    if(e1.get_health_points() > 0):
        print("Enemy 1 wins")
    else:
        print("Enemy 2 wins")

def hero_battle(hero: Hero, enemy: Enemy):
    while(hero.get_health_points() >0 and enemy.get_health_points() > 0):
        print('------')

        
        print(f'{hero.get_health_points()} HP')
        print(f'{enemy.get_health_points()} HP')
        print('')
       

        enemy.special_attack()
        enemy.attack()
        a1 = hero.get_health_points() - enemy.get_attack_damage()
        hero.set_health_points(a1)

        hero.attack()
        a2 = enemy.get_health_points() - hero.get_attack_damage()
        enemy.set_health_points(a2)

        print('---------')
        print('')

    if(hero.get_health_points() > 0):
        print("Hero wins")
    else:
        print("Enemy wins")

zombie = Zombie( 10, 1)
orge = Orge( 20, 3)
hero = Hero(10, 2)
weapon = Weapon('Sword', 5)
hero.equipWeapon()
hero_battle(hero, zombie)

