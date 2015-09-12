import random


total_heads = 0
total_tails = 0

count = 0

while (count < 1000000):
	result_of_toss = random.randint(1,2)

	if result_of_toss == 1:
		total_tails += 1
	elif result_of_toss == 2:
		total_heads += 1

	count +=1


print ('Total heads from 1000000 tosses = ', total_heads)
print ('Total tails from 1000000 tosses = ', total_tails)
