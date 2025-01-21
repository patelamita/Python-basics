"""
Assignment 1 
Count the Frequency of Characters
Write a function char_frequency(string) that takes a string as input and returns a dictionary with each character as the key and its frequency as the value.
Requirements:
- Ignore spaces and treat uppercase and lowercase letters as the same.
"""

def char_frequency(string):
    
    frequency = {}

    # Iterate through each character in the string
    for char in string:
        # Convert the character to lowercase
        char = char.lower()

        # Ignore spaces
        if char == " ":
            continue

        # Update the frequency in the dictionary
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

input_string = "Good Morning" 
print(char_frequency(input_string))

"""
Assignment 2: 
Reverse a Sentence
Write a function reverse_sentence(sentence) 
that takes a sentence as input and returns the sentence with the words reversed,
but the order of characters in each word preserved.
"""
def reverse_sentence(sentence):
    
    words = sentence.split()
    reversed_words = reversed(words)
    
    # Join the words back into a sentence
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

output = reverse_sentence("Hello world this is python")
print(output)  # Output: "Python is this world Hello"

"""Assignment 3 
Check Palindromes
Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward (ignoring spaces, punctuation, and capitalization).
Requirements:
- The function should handle uppercase and lowercase characters.
    """
    
def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    clean_string = ''.join(
        char.lower() for char in s if char.isalnum()  
    )
    
    return clean_string == clean_string[::-1]


print(is_palindrome("Racecar"))                        
print(is_palindrome("Amita"))                 
