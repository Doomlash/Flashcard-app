class A:
    p = 3


class B(A):

    @classmethod
    def func(cls):
        print(cls.p)


B.func()
