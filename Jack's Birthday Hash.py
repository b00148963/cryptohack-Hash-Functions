n = 1 << 11
# Initialize P as 1
P = 1
# Iterate through a range from 1 to n
for i in range(1, n):
    # Calculate the probability of an event occurring at 'i' trials using the formula
    # P = (1 - 1/n) ^ i
    P = pow((1 - 1/n), i)
    # Calculate the complementary probability
    nP = 1 - P
    # Check if the complementary probability is greater than 0.5 (50%)
    if nP > 0.5:
        print(i)
        break