# Write a function that takes a string as input and returns the highest value of consonant substrings.  
# Consonants are any letters of the alphabet except "aeiou".  We value a substring by the sum of the ASCII values of the consonants it contains.


def solve(s):
    vowels = "aeiou"
    highest_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            current_value += ord(char) - ord('a') + 1
        else:
            if current_value > highest_value:
                highest_value = current_value
            current_value = 0

    if current_value > highest_value:
        highest_value = current_value

    return highest_value
    # Example Usage
result_1 = solve("zodiacs")
result_2 = solve("strength")

print(f"The highest value of consonant substrings in 'zodiacs' is: {result_1}")
print(f"The highest value of consonant substrings in 'strength' is: {result_2}")
# The highest value of consonant substrings in 'zodiacs' is: 26
# The highest value of consonant substrings in 'strength' is: 57
# The function should return the highest value of the consonant substrings in the string.
# The function should return 0 if there are no consonant substrings.
# The function should return 0 if the string is empty.

