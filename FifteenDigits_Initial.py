import copy  # 调用copy库 为后续做元素位置交换做准备
from utils.Classes import grid
from utils.Functions import judgement
from utils.Functions import invertnum
from utils.Functions import solver

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