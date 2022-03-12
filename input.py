#get input from user
number_of_cans = input('how many cans of dog food do you want?\n')
#set bunny to can ratio
amount_of_bunnies_in_one_can = 2.7
#calculate
number_of_bunnies_to_order_from_farm = int(number_of_cans) * amount_of_bunnies_in_one_can
#output result to screen
print('You will need to order', number_of_bunnies_to_order_from_farm, 'bunnies')