class Animal:
	def speak(self):
		print("animal speaking...")
	def move(self):
		print("animal moving...")
		
class Cat(Animal):
	def speak(self):
		print("meow...")

	
jeff = Cat()

jeff.speak()

