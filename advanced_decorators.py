def decorator(*args, **kwargs):     # Takes the decorator arguments.
    def inner(func):                # Takes the function as a parameter.
        def wrapper():
            print('Decorator args:')
            for arg in args:
                print(f'\t{arg}')
            print('Decorator kwargs:')
            for key, value in kwargs.items():
                print(f'\t{key}: {value}')
            print(f'Calling {func.__name__}: ', end='')
            func()
        return wrapper
    return inner

@decorator('arg1', 'arg2', kwarg1='value_1', kwarg2='value_2')
def function():
    print('Hello, World!')
