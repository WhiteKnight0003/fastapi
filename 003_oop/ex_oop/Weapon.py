class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.__weapon_type = weapon_type
        self.__attack_increase = attack_increase
        
    # getter
    def get_weapon_type(self):
        return self.__weapon_type
    def get_attack_increase(self):
        return self.__attack_increase
    
    # setter
    def set_weapon_type(self, weapon_type):
        self.__weapon_type = weapon_type
    def set_attack_increase(self, attack_increase):
        self.__attack_increase = attack_increase
        