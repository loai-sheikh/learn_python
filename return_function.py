def basic_calc(number_1,number_2,operator):
    if operator == "+":
        return number_1+number_2
    elif operator == "-":
        return number_1-number_2
    elif operator == "*":
        return number_1*number_2
    elif operator == "/":
        return number_1/number_2
    else:
        return "bad operation!"

print(basic_calc(4,2,"*"))


def func_with_import(x):
    import random
    return random.randint(0,x)

print("random number: ",func_with_import(100))

def return_a_func(arg):
    def you_the_boss():
        print("boss!!")
    
    def you_loser():
        print("loser")
    
    if arg == "me":
        return you_the_boss
    else:
        return you_loser

func_from_func  = return_a_func("me")
func_from_func()