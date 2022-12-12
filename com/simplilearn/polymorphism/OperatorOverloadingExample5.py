class OperatorOverloadingExample4:

    # Home Work
    def __init__(self,name):
        self.name=name

    # +
    def __add__(self, other):
        return self.name+other.name

    # -
    #def __sub__(self, other):

    # *
    #def __mul__(self, other):

    # / // % ** += -= *= /= %= **= < <= > >=