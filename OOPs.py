import Functions


class N:
    def fun(self):
        print("Object Created in class")


Obj = N

N.fun(Obj)


#######################################################

class C:
    def __init__(self, Name, age):
        self.Name = Name
        self.age = age

    def fun(self):
        print("She is", self.Name, self.age)


Obj1 = C('Anuhya', 20)

Obj1.fun()


#########################################################

class C:
    def __init__(self):
        self.Name = "Bhargavi"
        self.age = 24

    def fun(self):
        self.Name = "Swathi"
        self.age = 23


Obj1 = C()
Obj2 = C()

print(Obj2.Name, Obj2.age)
Obj2.fun()


###########################################################

class Company:
    def __init__(self):
        print("Outer class Executed")

    class Block1:

        def __init__(self):
            print("Inner class executed")

        def fun(self):
            print("Block1 is IT Block")

    def Dep(self):
        print("There are Different Departments in Company")


C = Company()
S = C.Block1()
S.fun()
C.Dep()


###############################################################

class Myclass:
    def M1(self):
        print("Myclass is single inheritance")

    def M2(self):
        print("Myclass is single inheritance")


S = Myclass()
S.M1()


class Parent():
    def F1(self):
        print("Parent is Multi inheritance")


M = Parent()
M.F1()


class Child(Myclass, Parent):
    def Fun1(self):
        print("Child is multiple inheritance")


C = Child()
C.Fun1()


##############################################################
class Myclass:
    def __init__(self):
        print("Myclass init")

    def M1(self):
        print("Myclass is single inheritance")

    def M2(self):
        print("Myclass is single inheritance")


S = Myclass()
S.M1()


class Parent():

    def __init__(self):
        print("Parent init")

    def F1(self):
        print("Parent is Multi inheritance")


M = Parent()
M.F1()


class Child(Myclass, Parent):

    def __init__(self):
        super().__init__()
        print("Child init")

    def Fun1(self):
        print("Child is multiple inheritance")


C = Child()
C.F1()


###########################################################
class School:

    def Student(self):
        print("Going to School")


class College:

    def Student(self):
        print("In college days u know what u have to do.........")
        print("&")
        print("Having lot of fun with Friends")


class Teacher:
    def Class(self, Stu):
        Stu.Student()


S = School()
C = College()
T = Teacher()
T.Class(C)


##############################################################

class Operator_overload:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __mul__(self, other):
        A = self.X * other.X
        B = self.Y * other.Y
        Z = Operator_overload(A, B)
        return Z


S = Operator_overload(35, 15)
T = Operator_overload(46, 20)
Z = S * T
print(Z.Y)


# + T.Y)
# print(S.X * T.X)
# print(T.X + S.X)
# print(T.Y + S.Y)
##############################################################

class Method_overloading:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self, a, b):
        M = a + b
        return M


A = Method_overloading(67, 34)
print(A.Add(76, 34))


######################################################

class A:
    def Over_Riding(self):
        print('In A class')


class B(A):
    def Method(self):
        print('In B class')


Z = B()
Z.Over_Riding()

#########################################################

from abc import ABC, abstractmethod


class College(ABC):
    @abstractmethod
    def Lecture(self):
        pass


class Student(College):
    def Lecture(self):
        print("Teaches class")


class VP:

    def Head(self, y):
        print("Head of the College")
        y.Lecture()


# T = College()
# T.method()

X = Student()
# X.Lecture()

Obj = VP()
Obj.Head(X)

########################################################

Values = 1, 2, 3, 4, 5

Val = iter(Values)

print(next(Val))
print(next(Val))
print(next(Val))
print(next(Val))


########################################################
class Values:

    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):

        if self.x <= 20:
            z = self.x
            self.x += 4
            return z
        else:
            raise StopIteration


Numbers = Values()

for i in Numbers:
    print(i)

Num_Iter = iter(Numbers)
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))
print(next(Numbers))


####################################################

class Number:

    def __iter__(self):
        self.j = 1
        return self

    def __next__(self):
        if self.j <= 10:
            N = self.j * self.j
            self.j += 1
            return N
        else:
            raise StopIteration


Values = Number()
for i in Values:
    print(i)

Val_iter = iter(Values)
print(next(Val_iter))
print(next(Values))
print(next(Values))


#######################################################

def Method():
    n = 11
    while n <= 20:
        x = n * n
        yield x
        n += 1


Generator = Method()
for Sqrs in Generator:
    print(Sqrs)

#########################################################

# a = 4
a = 0
b = 9

try:
    print("In Try")
    print(b / a)

except Exception:
    print("We can't divide 'a',because it's value is zero")

finally:
    print("In Finally")

########################################################

from time import sleep
from threading import *


class T1(Thread):
    def run(self):
        for i in range(3):
            print("It is from Function1")


class T2(Thread):
    def run(self):
        for i in range(3):
            print("It is from Function2")


M1 = T1()
M2 = T2()

M1.start()
sleep(2)
M2.start()

##########################################################


f = open("C:\\Cust_file1.txt", 'r')
print(f.read())
f.close()

f = open("C:\\Cust_file3.txt", 'r')
for i in f:
    print(f.readlines())
f.close()

f = open("Customer Details", 'r')
print(f.read())
f.close()


##########################################################

def Linear_Search(List, Key):
    i = 0
    while i < len(List):
        if List[i] == Key:
            return True
        i = i + 1
    return False


List = [2, 4, 6, 8, 10, 12, 14, 16]
Key = 12
if Linear_Search(List, Key):
    print("Found")
else:
    print('Not Found')


def Linear_Search(List, Key):
    for i in range(len(List)):
        if Key == List[i]:
            print('Number found')
            break
    else:
        print('Number not found')


List = [45, 23, 78, 67, 23]
Key = 23
Linear_Search(List, Key)


#######################################################


# def Binary_Search(Values, num):
#  lower = 0
#  upper = len(Values) - 1
#  mid = 0
#    while lower < upper:
# mid = (lower + upper) // 2
# if num == Values[mid]:
#     print("num found in Values")
#  else:
#       print("num not found in Values")
#        return True
# else:
#    if num > Values[mid]:
#       lower = mid + 1
#     else:
#          upper = mid - 1
#       return False


# Values = [2, 4, 16, 25, 36, 47, 52, 63]
# num = 4

# Binary_Search(Values, num)


###########################################################

# pos = -1


# def Sort(list, n):
#    lower = 0
#    upper = len(list) - 1

#    while lower < upper:
#        mid = (lower + upper) // 2
#        if n == list[mid]:
#           globals()['pos'] = mid
#            return True
#        elif n > list[mid]:
#            lower = mid + 1
#        else:
#            upper = mid - 1
#            return False


# list = [20, 31, 42, 59, 14, 64, 77, 81]
# n = 60

# if Sort(list, n):
#    print("Number found at", pos + 1)
# else:
#    print("Number not found")


#########################################################

def Bubble_sort(List):
    for i in range(len(List) - 1):
        for j in range(len(List) - 1):
            if (List[j] > List[j + 1]):
                temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = temp


List = [36, 78, 2, 8, 44]
print(List)
Bubble_sort(List)
print(List)


###########################

def Bs(Values):
    for i in range(len(Values) - 1, 0, -1):
        for j in range(len(Values) - 1):
            if (Values[j] > Values[j + 1]):
                temp = Values[j]
                Values[j] = Values[j + 1]
                Values[j + 1] = temp


Values = [89, 75, 62, 58, 46, 32, 27, 93]
print(Values)
Bs(Values)
print(Values)


###########################################################


def selection_sort(Val):
    for i in range(6):
        minpos = i
        for j in range(i, 7):
            if Val[j] < Val[minpos]:
                minpos = j

            temp = Val[i]
            Val[i] = Val[minpos]
            Val[minpos] = temp
        print(Val)


Val = [5, 8, 3, 2, 6, 9, 1]
print(Val)
selection_sort(Val)
print(Val)
