class Myclass:
    def M1(self):
        print("Myclass is single inheritance")

    def M2(self):
        print("Myclass is single inheritance")


S = Myclass()
S.M1()


class Parent(Myclass):
    def F1(self):
        print("Parent is Multi inheritance")


M = Parent()
M.F1()


class A():
    def F1(self):
        print("A is Single inheritance")


M = A()
M.F1()


class B:
    def F2(self):
        print("B is Single inheritance")


M = B()
M.F2()


class Child(A, B):
    def Fun1(self):
        print("Child class is multiple inheritance")


C = Child()
C.Fun1()