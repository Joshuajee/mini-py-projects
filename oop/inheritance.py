class LivingThings:
    type = None
    is_alive = True
    strength = 50
    
    def __init__(self, type, strength):
        self.type = type
        self.strength = strength
    
    
    def die(self):
        self.is_alive = False
    
    def eat(self, food):
        print(type(food))
        food.die()
        self.strength += food.strength
        food.strength = 0


class Bird(LivingThings):
    is_flying = False
    def fly(self):
        self.is_flying = True
    def stop_flight(self):
        self.is_flying = False
        

bird = Bird("Bird", 50)
horse = LivingThings("Horse", 200)

print(bird.type, horse.type)
print(bird.is_alive)

