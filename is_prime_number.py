def is_prime(value, next_num = 0):
    if next_num ==0:
        next_num = value -1
    else:
        next_num -= 1
    return True if next_num == 1 else value % next_num !=0 and is_prime(value, next_num) 

print(is_prime(4))
