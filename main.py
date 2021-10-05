from builtins import set
from collections import deque
from copy import deepcopy
import random


class puzzle:
    p = [[1, 2, 3], [4, 5, 6], [7, 8, 0], 0, 0, [""]]
    stack = []
    queue = deque([])
    p_solve = []

    def __init__(self):
        print("\n*****************************")
        print("GOAL:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 0]\n")
        print("Select the input type: ")
        print("1- Keyboard\n2- Open File\n3- Random")
        menu = int(input("please enter number: "))
        if menu == 1:
            for x in range(3):
                for y in range(3):
                    print(" enter puzzle[", x, "][", y, "]: ")
                    self.p[x][y] = int(input())
            self.myprint(self.p)
            self.p[3] = 1
            self.p[4] = 1
        if menu == 3:
            self.myrandom()
        if menu == 2:
            self.openfile()

    def openfile(self):
        f = open("demofile.txt", "r")
        for x in range(3):
            for y in range(3):
                for x1 in f.readline(1):
                    self.p[x][y] = int(x1)

    def myrandom(self):
        number = int(input("please inter move number: "))
        a = 0
        while a < number:
            if self.p[0][0] == 0:
                x = random.randint(0, 1)
                if x == 0:
                    self.p[0][0] = self.p[1][0]
                    self.p[0][0] = 0
                if x == 1:
                    self.p[0][0] = self.p[0][1]
                    self.p[0][1] = 0
            if self.p[0][1] == 0:
                x = random.randint(0, 2)
                if x == 0:
                    self.p[0][1] = self.p[1][1]
                    self.p[1][1] = 0
                if x == 1:
                    self.p[0][1] = self.p[0][0]
                    self.p[0][1] = 0
                if x == 2:
                    self.p[0][1] = self.p[0][2]
                    self.p[0][2] = 0
            if self.p[0][2] == 0:
                x = random.randint(0, 1)
                if x == 0:
                    self.p[0][2] = self.p[1][2]
                    self.p[1][2] = 0
                if x == 1:
                    self.p[0][2] = self.p[0][1]
                    self.p[0][1] = 0
            if self.p[1][0] == 0:
                x = random.randint(0, 2)
                if x == 0:
                    self.p[1][0] = self.p[0][0]
                    self.p[0][0] = 0
                if x == 1:
                    self.p[1][0] = self.p[2][0]
                    self.p[2][0] = 0
                if x == 2:
                    self.p[1][0] = self.p[1][1]
                    self.p[1][1] = 0
            if self.p[1][1] == 0:
                x = random.randint(0, 3)
                if x == 0:
                    self.p[1][1] = self.p[0][1]
                    self.p[0][1] = 0
                if x == 1:
                    self.p[1][1] = self.p[2][1]
                    self.p[2][1] = 0
                if x == 2:
                    self.p[1][1] = self.p[1][0]
                    self.p[1][0] = 0
                if x == 3:
                    self.p[1][1] = self.p[1][2]
                    self.p[1][2] = 0
            if self.p[1][2] == 0:
                x = random.randint(0, 2)
                if x == 0:
                    self.p[1][2] = self.p[0][2]
                    self.p[0][2] = 0
                if x == 1:
                    self.p[1][2] = self.p[2][2]
                    self.p[2][2] = 0
                if x == 2:
                    self.p[1][2] = self.p[1][1]
                    self.p[1][1] = 0
            if self.p[2][0] == 0:
                x = random.randint(0, 1)
                if x == 0:
                    self.p[2][0] = self.p[1][0]
                    self.p[1][0] = 0
                if x == 1:
                    self.p[2][0] = self.p[2][1]
                    self.p[2][1] = 0
            if self.p[2][1] == 0:
                x = random.randint(0, 2)
                if x == 0:
                    self.p[2][1] = self.p[1][1]
                    self.p[1][1] = 0
                if x == 1:
                    self.p[2][1] = self.p[2][0]
                    self.p[2][0] = 0
                if x == 2:
                    self.p[2][1] = self.p[2][2]
                    self.p[2][2] = 0
            if self.p[2][2] == 0:
                x = random.randint(0, 1)
                if x == 0:
                    self.p[2][2] = self.p[1][2]
                    self.p[1][2] = 0
                if x == 1:
                    self.p[2][2] = self.p[2][1]
                    self.p[2][1] = 0
            a += 1
        self.myprint(self.p)

    def solve(self):
        print("1. Depth First Search\n2. Breadth First Search\n3. Iterative deepening depth-first search")
        select = int(input("Enter your choice: "))
        if (select == 1 or select == 2):
            level = int(input("Enter level for advance: "))
        p2 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        if select == 1:
            if self.equal(p2, self.p):
                print(" it's right ")
                self.myprint(self.p)
                exit()
            self.stack.append(self.p)
            while 1:
                p3 = self.stack.pop()
                counter = p3[3]
                if counter <= level:
                    counter += 1
                if self.equal(p3, p2):
                    self.myprint(p3)
                    self.p_solve = deepcopy(p3)
                    break
                p_up = deepcopy(p3)
                p_down = deepcopy(p3)
                p_right = deepcopy(p3)
                p_left = deepcopy(p3)
                for i in range(3):
                    for j in range(3):
                        if p3[i][j] == 0:
                            x = i
                            y = j
                if x != 0 and counter <= level and p3[5][-1] != "down":
                    p_up[x][y] = p_up[x - 1][y]
                    p_up[x - 1][y] = 0
                    p_up[4] = 1
                    p_up[3] = counter
                    p_up[5].append("up")
                else:
                    p_up[4] = 0
                if x != 2 and counter <= level and p3[5][-1] != "up":
                    p_down[x][y] = p_down[x + 1][y]
                    p_down[x + 1][y] = 0
                    p_down[3] = counter
                    p_down[4] = 1
                    p_down[5].append("down")
                else:
                    p_down[4] = 0
                if y != 2 and counter <= level and p3[5][-1] != "left":
                    p_right[x][y] = p_right[x][y + 1]
                    p_right[x][y + 1] = 0
                    p_right[3] = counter
                    p_right[4] = 1
                    p_right[5].append("right")
                else:
                    p_right[4] = 0
                if y != 0 and counter <= level and p3[5][-1] != "right":
                    p_left[x][y] = p_left[x][y - 1]
                    p_left[x][y - 1] = 0
                    p_left[3] = counter
                    p_left[4] = 1
                    p_left[5].append("left")
                else:
                    p_left[4] = 0
                if p_left[4] == 1 and counter <= level:
                    self.stack.append(p_left)
                if p_right[4] == 1 and counter <= level:
                    self.stack.append(p_right)
                if p_down[4] == 1 and counter <= level:
                    self.stack.append(p_down)
                if p_up[4] == 1 and counter <= level:
                    self.stack.append(p_up)

        if select == 2:
            if self.equal(p2, self.p):
                print(" it's right ")
                self.myprint(self.p)
                exit()
            self.queue.append(self.p)
            while 1:
                p3 = self.queue.popleft()
                counter = p3[3]
                if counter <= level:
                    counter += 1
                if self.equal(p3, p2):
                    self.myprint(p3)
                    self.p_solve = deepcopy(p3)
                    break
                p_up = deepcopy(p3)
                p_down = deepcopy(p3)
                p_right = deepcopy(p3)
                p_left = deepcopy(p3)
                for i in range(3):
                    for j in range(3):
                        if p3[i][j] == 0:
                            x = i
                            y = j
                if x != 0 and counter <= level and p3[5][-1] != "down":
                    p_up[x][y] = p_up[x - 1][y]
                    p_up[x - 1][y] = 0
                    p_up[4] = 1
                    p_up[3] = counter
                    p_up[5].append("up")
                else:
                    p_up[4] = 0
                if x != 2 and counter <= level and p3[5][-1] != "up":
                    p_down[x][y] = p_down[x + 1][y]
                    p_down[x + 1][y] = 0
                    p_down[3] = counter
                    p_down[4] = 1
                    p_down[5].append("down")
                else:
                    p_down[4] = 0
                if y != 2 and counter <= level and p3[5][-1] != "left":
                    p_right[x][y] = p_right[x][y + 1]
                    p_right[x][y + 1] = 0
                    p_right[3] = counter
                    p_right[4] = 1
                    p_right[5].append("right")
                else:
                    p_right[4] = 0
                if y != 0 and counter <= level and p3[5][-1] != "right":
                    p_left[x][y] = p_left[x][y - 1]
                    p_left[x][y - 1] = 0
                    p_left[3] = counter
                    p_left[4] = 1
                    p_left[5].append("left")
                else:
                    p_left[4] = 0
                if p_up[4] == 1 and counter <= level:
                    self.queue.append(p_up)
                if p_down[4] == 1 and counter <= level:
                    self.queue.append(p_down)
                if p_right[4] == 1 and counter <= level:
                    self.queue.append(p_right)
                if p_left[4] == 1 and counter <= level:
                    self.queue.append(p_left)

        if select == 3:
            limit = 1
            self.stack.append(self.p)
            while 1:
                if len(self.stack) == 0:
                    limit = limit + 1
                    self.stack.append(self.p)
                    print("increase limit")
                    continue
                p3 = self.stack.pop()
                counter = p3[3]
                if counter <= limit:
                    counter += 1
                if self.equal(p3, p2):
                    self.myprint(p3)
                    self.p_solve = deepcopy(p3)
                    break
                p_up = deepcopy(p3)
                p_down = deepcopy(p3)
                p_right = deepcopy(p3)
                p_left = deepcopy(p3)
                for i in range(3):
                    for j in range(3):
                        if p3[i][j] == 0:
                            x = i
                            y = j
                if x != 0 and counter <= limit and p3[5][-1] != "down":
                    p_up[x][y] = p_up[x - 1][y]
                    p_up[x - 1][y] = 0
                    p_up[4] = 1
                    p_up[3] = counter
                    p_up[5].append("up")
                else:
                    p_up[4] = 0
                if x != 2 and counter <= limit and p3[5][-1] != "up":
                    p_down[x][y] = p_down[x + 1][y]
                    p_down[x + 1][y] = 0
                    p_down[3] = counter
                    p_down[4] = 1
                    p_down[5].append("down")
                else:
                    p_down[4] = 0
                if y != 2 and counter <= limit and p3[5][-1] != "left":
                    p_right[x][y] = p_right[x][y + 1]
                    p_right[x][y + 1] = 0
                    p_right[3] = counter
                    p_right[4] = 1
                    p_right[5].append("right")
                else:
                    p_right[4] = 0
                if y != 0 and counter <= limit and p3[5][-1] != "right":
                    p_left[x][y] = p_left[x][y - 1]
                    p_left[x][y - 1] = 0
                    p_left[3] = counter
                    p_left[4] = 1
                    p_left[5].append("left")
                else:
                    p_left[4] = 0
                if p_left[4] == 1 and counter <= limit:
                    self.stack.append(p_left)

                if p_right[4] == 1 and counter <= limit:
                    self.stack.append(p_right)

                if p_down[4] == 1 and counter <= limit:
                    self.stack.append(p_down)

                if p_up[4] == 1 and counter <= limit:
                    self.stack.append(p_up)

    def myprint(self, p4):
        for item in p4:
            print(item, "\n")

    def equal(self, p5, p6):
        if p5[0] == p6[0] and p5[1] == p6[1] and p5[2] == p6[2]:
            return True
        else:
            return False

    def print_solve(self):
        for item in self.p_solve[5]:
            print(item, "\n")
            for i in range(3):
                for j in range(3):
                    if self.p[i][j] == 0:
                        x = i
                        y = j
            if item == "up":
                self.p[x][y] = self.p[x - 1][y]
                self.p[x - 1][y] = 0
                self.myprint(self.p)
            if item == "down":
                self.p[x][y] = self.p[x + 1][y]
                self.p[x + 1][y] = 0
                self.myprint(self.p)
            if item == "right":
                self.p[x][y] = self.p[x][y + 1]
                self.p[x][y + 1] = 0
                self.myprint(self.p)
            if item == "left":
                self.p[x][y] = self.p[x][y - 1]
                self.p[x][y - 1] = 0
                self.myprint(self.p)


game = puzzle()
game.solve()
game.print_solve()
