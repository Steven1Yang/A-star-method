import copy  # 调用copy库 为后续做元素位置交换做准备


class grid:
    def __init__(self,state):
        self.prestate = None
        self.target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        self.state = state
        self.upgrade()
        self.find0()

    def upgrade(self):
        if self.prestate is not None:
            self.G = self.prestate.G+1
        else:
            self.G = 0
        self.H = 0
        for i in range(4):
            for j in range(4):
                targetposition = self.target[i][j]
                currentposition = self.findx(targetposition)
                self.H += abs(currentposition[0] - i) + abs(currentposition[1] - j)
        self.F = self.G + self.H

    def findx(self, x):
        for i in range(4):
            if (x in self.state[i]):
                j = self.state[i].index(x)
                return [i, j]

    def find0(self):
        self.zero = self.findx(0)

    def move(self, deltarow, deltacol):
        newstate = copy.deepcopy(self.state)
        temporarystate = self.state[self.zero[0]+deltarow][self.zero[1]+deltacol]
        newstate[self.zero[0]][self.zero[1]] = temporarystate
        newstate[self.zero[0]+deltarow][self.zero[1]+deltacol] = 0
        return newstate

    def newproductstate(self):
        processlist = []
        row0 = self.zero[0]
        col0 = self.zero[1]
        if row0 == 0 or row0 == 1 or row0 == 2:  # 将0向下移动
            processlist.append(self.move(1, 0))
        if row0 == 1 or row0 == 2 or row0 == 3:  # 将0向上移动
            processlist.append(self.move(-1, 0))
        if col0 == 0 or col0 == 1 or col0 == 2:  # 将0向右移动
            processlist.append(self.move(0, 1))
        if col0 == 1 or col0 == 2 or col0 == 3:  # 将0向左移动
            processlist.append(self.move(0, -1))
        return processlist

    def see(self):
        for i in range(4):
             print(self.state[i])
        print("F=",self.F,"G=",self.G,"H=",self.H)
        print("*"*10)

    def seeAns(self):
        ans=[]
        ans.append(self)
        p=self.prestate
        while(p):
            ans.append(p)
            p=p.prestate
        ans.reverse()
        for i in ans:
            i.see()

def judgement(obj, objlist):
    objstate = obj.state
    statelist = []
    for i in objlist:
        statelist.append(i.state)
    if objstate in statelist:
        result = [True, statelist.index(objstate)]
    else:
        result = [False, 0]
    return result


def invertnum(grid):
    nums = [i for item in grid for i in item]
    invertnum = 0
    for i in range(len(nums)):
        if (nums[i] != 0):
            for j in range(i):
                if nums[j] > nums[i]:
                    invertnum += 1
    return invertnum


def solver(given,target):
    invertnumgiven = invertnum(given)
    invertnumtarget = invertnum(target)
    if (invertnumgiven%2 == invertnumtarget%2):
        return True
    else:
        return False


def Astarsolver(startstate):
    openlist = []
    closelist = []
    duixiang = grid(startstate)
    target=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    if (solver(startstate, target) != True):
        print("该十五数码问题无解")
        exit(1)
    openlist.append(duixiang)
    searchtime = 0
    while (openlist):
        openlist.sort(key=lambda G:G.F)
        minf = openlist[0]
        if (minf.H == 0):
            print('搜索时间:', searchtime, '探索深度4：', minf.G)
            minf.seeAns()
            break
        openlist.pop(0)
        closelist.append(minf)
        newstate = minf.newproductstate()
        for state in newstate:
            tmpG=grid(state)
            tmpG.prestate=minf
            tmpG.upgrade()
            findstate=judgement(tmpG,openlist)
            findstate2=judgement(tmpG,closelist)
            if(findstate2[0]==True and tmpG.F<closelist[findstate2[1]].F):
                closelist[findstate2[1]]=tmpG
                openlist.append(tmpG)
                searchtime+=1
            if(findstate[0]==True and tmpG.F<openlist[findstate[1]].F):
                openlist[findstate[1]]=tmpG
                searchtime+=1
            if(findstate[0]==False and findstate2[0]==False):
                openlist.append(tmpG)
                searchtime+=1
state = []
for i in range(4):
    row = []
    for j in range(4):
        element = int(input("请输入矩阵的元素 ({}, {})：".format(i, j)))
        row.append(element)
    state.append(row)
print("您输入的矩阵是：")
for row in state:
    for element in row:
        print(element, end=" ")
    print()
Astarsolver(state)
