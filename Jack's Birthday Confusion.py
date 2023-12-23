from math import factorial
n = 2048
for i in range(n):
	# Calculate the probability using the formula
	prob = 1 - factorial(n) / (factorial(n - i)*pow(n,i))
	# Check if the probability exceeds 0.75
	if prob > 0.75:
		print(i)
		break