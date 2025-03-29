from Enemy import *
import random

class Orge(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__('Orge' , health_points, attack_damage)
    
    def talk(self):
        print('Orge is slamming hands all around')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.set_health_points(self.get_health_points() + 4)
            print('Orge attack has increased by 4 !')