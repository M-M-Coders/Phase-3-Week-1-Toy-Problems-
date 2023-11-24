# Function to check if there are two positive values among three integers
def two_positives(a, b, c):
    positives = 0

    if a > 0:
        positives += 1

    if b > 0:
        positives += 1

    if c > 0:
        positives += 1

    return positives == 2

# Test the function with some examples
print(two_positives(1, 2, 3))
print(two_positives(1, -1, 1))
print(two_positives(-1, -2, -3))
print(two_positives(1, 2, -3))
print(two_positives(1, -2, -3))
print(two_positives(-1, -2, 3))
print(two_positives(0, 1, 2))
print(two_positives(0, 0, 0))
print(two_positives(0, 0, 1))