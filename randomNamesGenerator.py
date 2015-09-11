import random

class RandomName():

	list1 = ['Ar', 'Gor', 'Mak', 'Vlo', 'Dur', 'Mur'];
	list2 = ['nak', 'vok', 'nik', 'stu', 'an', 'bin'];

	def GenerateRandomName(self):
		val1 = random.choice(self.list1)
		val2 = random.choice(self.list2)
		print (val1)
		print (val2)
		return val1 + val2;


rand = RandomName()
result = rand.GenerateRandomName()

print(result)