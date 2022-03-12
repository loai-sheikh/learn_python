def func_with_only_1_default_arg_val(val_1,val_2,val_3="default arg value"):
    print(val_1)
    print(val_2)
    print(val_3)

func_with_only_1_default_arg_val(val_3="01",val_2="02",val_1="03")

def func_with_x_args(*args):
    print(type(args))
    for i in args:
        print(i)

func_with_x_args(1,"banana","mishmish","apple")

def my_func(a,b,c,d,e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

x=(1,2,3,4,5)
my_func(*x)