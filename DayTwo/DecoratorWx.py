class logger:
    def __init__(self, fun):
        self.fun = fun
    def __call__(self, *args, **kwargs):
        retvaule = self.fun(*args)
        print('Calling {} function with {} input and return is {}'.format(self.fun.__name__,
                                                                 args,
                                                                 retvaule))
        return retvaule


@logger
def multiple(a,b):
    return a*b

print(multiple(4,5))