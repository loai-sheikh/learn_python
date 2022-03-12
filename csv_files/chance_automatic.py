from termcolor import colored
import random

CHANCE_VALUES = [7,8,9,10,'J','Q','K','A']
draws = 1
print('Enter number of draws:')
draws = int(input())
print(
    '\u2660',
    colored('\u2665\ufe0f', 'red'),
    colored('\u2666\ufe0f', 'red'),
    '\u2663'
    )
for i in range(draws):
    print(
        random.choice(CHANCE_VALUES),
        random.choice(CHANCE_VALUES),
        random.choice(CHANCE_VALUES),
        random.choice(CHANCE_VALUES)
        )