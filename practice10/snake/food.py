import random

def generate_food(snake, width, height):
    while True:
        food = (
            random.randrange(0, width, 20),
            random.randrange(0, height, 20)
        )
        if food not in snake:
            return food