import random as rnd

#print(rnd.randint(0,100))

def roll_dice():
    print('Dice 1:',rnd.randint(1,6))
    print('Dice 2:',rnd.randint(1,6),'\n' )

roll_dice()

my_list = ['Apple','Bannana','Orange','peach']
print(rnd.choice(my_list))
print(rnd.choices(my_list,k=2))
