from Weapon import *

class Hero:
    def __init__(self, health_points, attack_damage):
        self.__health_points = health_points
        self.__attack_damage = attack_damage
        self.is_weapon_quipped = False
        self.weapon: Weapon = None

    def equipWeapon(self):
        if self.weapon is not None and not self.is_weapon_quipped:
            self.__attack_damage += self.weapon.get_attack_increase()
            self.is_weapon_quipped = True      

    def attack(self):
        print('Hero attacks for {self.__attack_damage} damage.')

    # getter
    def get_health_points(self):
        return self.__health_points
    def get_attack_damage(self):
        return self.__attack_damage
    
    # setter
    def set_health_points(self, health_points):
        self.__health_points = health_points
    def set_attack_damage(self, attack_damage):
        self.__attack_damage = attack_damage
