import re

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
    def as3(self):
        for i,j in enumerate(range(100,0,-1),1):
            if i == 100:
                print(j)
            else:
                print(j,end=", ")
#-----------------------課題４------------------------------------
    def as4(self):
        while True:
            num = input("整数を入力してください(終了する場合はe)\n")
            find = re.search(r"[^\-0-9]",num)
            if num == "e":
                break
            elif find:
                print("正しい値を入力してください")
                continue
            else:
                num = int(num)
                if num % 2 == 0:
                    print("偶数です")
                else:
                    print("奇数です")
#-----------------------課題５------------------------------------
    def as5(self):
        while True:
            num = input("総和を出したい最大の整数を入力してください(終了する場合はe)\n")
            find = re.search(r"[^-0-9]",num)
            if num == "e":
                break
            elif find:
                print("正しい値を入力してください")
            else:
                ans = 0
                if int(num) <= 0:
                    for i in range(1,int(num)-1,-1):
                        ans += i
                else:
                    ans = int(num)*(int(num)+1)/2
                print(int(ans))


assignments = Assignments()
assignments.as5()
