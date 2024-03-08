class Car:
    
    def max_speed(self):
        pass
    

class Toyota(Car):
    
    def max_speed(self):
        return 200
    

class Mercedes(Car):
    
    def max_speed(self):
        return 250

toyota = Toyota()

print(toyota.max_speed())

mercedes = Mercedes()

print(mercedes.max_speed())