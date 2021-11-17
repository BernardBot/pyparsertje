class A():
    def __init__(self):
        self.a = 10
        self.b = 20

    def __str__(self):
        attrs = [k + "=" + str(v) for k, v in vars(self).items()]
        return self.__class__.__name__ + "(" + ",".join(attrs) + ")"
a = A()
print(a)
