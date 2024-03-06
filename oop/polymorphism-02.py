class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("I can fly.")


class sparrow(Bird):
    
	def intro(self):
		print("I am Sparrow")
    

	# def flight(self):
	# 	print("Sparrows can fly.")

class ostrich(Bird):
    
	def intro(self):
		print("I am Ostrich")

	def flight(self):
		print("Ostriches cannot fly.")

	

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
