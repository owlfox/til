def test_var_args(f_arg, *argv):
    '''
    argument with varible length.
    '''
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

def greet_me(**kwargs):
    '''
    pass in a variable length key value pair as argument.
    '''
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="Michael", name2="Ace")
