from random import choice

class RandomName():

	list1 = ['Ar', 'Gor', 'Mak', 'Vlo', 'Dur', 'Mur'];
	list2 = ['nak', 'vok', 'nik', 'stu', 'an', 'bin'];

	def GenerateRandomName(self):
		val1 = choice(self.list1)
		val2 = choice(self.list2)
		
		return val1 + val2;

rand = RandomName()
result = rand.GenerateRandomName()

print(result)