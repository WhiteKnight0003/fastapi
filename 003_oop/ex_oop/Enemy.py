class Enemy:
    

    def __init__(self, type_of_enemy , health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.__health_points = health_points
        self.__attack_damage = attack_damage
        
    def talk(self):
        print(f"I am a {self.__type_of_enemy} . Be prepared to fight")

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you .')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.__attack_damage} damage.')

    def special_attack(self):
        print('Enemy has no special attack.')
    
    
    # getter
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    def get_health_points(self):
        return self.__health_points
    def get_attack_damage(self):
        return self.__attack_damage
    
    # setter
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy
    def set_health_points(self, health_points):
        self.__health_points = health_points
    def set_attack_damage(self, attack_damage):
        self.__attack_damage = attack_damage    