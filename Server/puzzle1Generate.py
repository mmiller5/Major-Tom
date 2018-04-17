import random
import string


def puzzle1Generate():
    solution = random.choice(string.ascii_uppercase)
    return solution
    
print(puzzle1Generate())