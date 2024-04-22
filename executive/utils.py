# utils.py
import random
import string

def custom_randomizer():
    # Define the pool of characters for randomization
    pool = string.ascii_letters + string.digits + string.punctuation
    # Return a randomly chosen character from the pool
    return random.choice(pool)

def substitute_characters(data):
    substituted_data = ''.join(custom_randomizer() if char.isalpha() else char for char in data)
    return substituted_data

def obfuscate(data):
    obfuscated_data = data[::-1] 
    return obfuscated_data
