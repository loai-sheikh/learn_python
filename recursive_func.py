def recursive_func(num):
    if num<=10:
        print('recursive_func recursion #',num)
        recursive_func(num+1)
    else: 
        print('final function call!!')
    print('after call to recursive func #',num)

recursive_func(1)