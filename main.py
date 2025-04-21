# main.py

animal_legs ={
    'lion':4,
    'deer':4,
    'elephant':4,
    'horse':4,
    'dog':4,
    'cat':4,
    'monkey':2,
    'parrot':2,
    'ostrich':2,
    'snake':0,
    'worm':0,
    'spider':8,
    'ant':6,
    'centipede':100,
    'frog':4,
    }
def count_four_legged_animals(animals):
    return sum(1 for animal in animals if animal_legs.get(animal, -1) == 4)