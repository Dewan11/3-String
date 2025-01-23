def count_vowels(input_string):
    vowels = "aeiouAEIOU"  
    return sum(char in vowels for char in input_string)
    
user_input = input("Please enter a string: ")
vowel_count = count_vowels(user_input)

print(f"The number of vowels is: {vowel_count}")
