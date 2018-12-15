a = 10
def func():
    pass

print('--- locals for main ---')
print(locals())
print('------------------')

def loc_func():
    v = 123
    print('--- locals for loc_func ---')
    print(locals())
    print('------------------')

def loc_func_args(param):
    v = 123
    print('--- locals for loc_func_args ---')
    print(locals())
    print('------------------')


loc_func()
loc_func_args("hello")
    