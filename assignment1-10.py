
class Assignments:
    def as1(self):
        for i,j in enumerate(range(1,101),1):
            if i == 100:
                print(j)
            else:
                print(j,end=", ")

assignments = Assignments()
assignments.as1()
