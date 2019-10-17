
class Assignments:
#-----------------------課題１------------------------------------
    def as1(self):
        for i,j in enumerate(range(1,101),1):
            if i == 100:
                print(j)
            else:
                print(j,end=", ")
#-----------------------課題２------------------------------------
    def as2(self):
        for i in range(1,101):
            if i % 15 == 0:
                print(i,"FizzBuzz")
            elif i % 3 == 0:
                print(i,"Fizz")
            elif i % 5 == 0:
                print(i,"Buzz")
            else:
                print(i)
#-----------------------課題３------------------------------------

assignments = Assignments()
assignments.as2()
