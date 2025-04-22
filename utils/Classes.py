import copy

class State(object):
    def __init__(self, deepth=0, rest_dis=0.0, state=None, hash_value=None, father_node=None):
        '''
        初始化
        :参数 deepth: 从初始节点到目前节点所经过的步数
        :参数 rest_dis: 启发距离
        :参数 state: 节点存储的状态 4*4的列表
        :参数 hash_value: 哈希值，用于判重
        :参数 father_node: 父节点指针
        '''
        self.deepth = deepth
        self.rest_dis = rest_dis
        self.fn = self.deepth + self.rest_dis
        self.child = []  # 孩子节点
        self.father_node = father_node  # 父节点
        self.state = state  # 局面状态
        self.hash_value = hash_value  # 哈希值

    def __lt__(self, other):  # 用于堆的比较，返回距离最小的
        return self.fn < other.fn

    def __eq__(self, other):  # 相等的判断
        return self.hash_value == other.hash_value

    def __ne__(self, other):  # 不等的判断
        return not self.__eq__(other)


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
