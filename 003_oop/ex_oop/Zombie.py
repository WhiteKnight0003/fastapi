from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__('Zombie' , health_points, attack_damage)

    def tank(self):
        print('*Grumbling ... *')
    
    def spread_disease(self):
        print('The Zombie is trying to spread infection.')
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.set_health_points(self.get_health_points() + 2)
            print('Zombie regenerates 2 HP!')