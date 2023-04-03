class run:
    @classmethod
    def leifangfa(cls, a):
        print("一个类方法", a)


run.leifangfa(123)

A = run()
A.leifangfa(456)

B = run.leifangfa
B(999)


class C(run):
    pass


C.leifangfa(int(666))




