import heapq
import copy
import math
from utils.Classes import State
# 上下左右四个方向移动
MOVE = {'up': [1, 0],
        'down': [-1, 0],
        'left': [0, -1],
        'right': [0, 1]}

# OPEN表
OPEN = []
def cal_M_distence(cur_state, SG):
    '''
    计算曼哈顿距离
    :参数 state: 当前状态,4*4的列表, State.state
    :返回: M_cost 每一个节点计算后的曼哈顿距离总和
    '''
    M_cost = 0
    for i in range(4):
        for j in range(4):
            if cur_state[i][j] == SG[i][j]:
                continue
            num = cur_state[i][j]
            if num == 0:
                x, y = 3, 3
            else:
                x = num / 4  # 理论横坐标
                y = num - 4 * x - 1  # 理论的纵坐标
                M_cost += (abs(x - i) + abs(y - j))
    return M_cost

def cal_E_distence(cur_state,SG):
    '''
    计算曼哈顿距离
    :参数 state: 当前状态,4*4的列表, State.state
    :返回: M_cost 每一个节点计算后的曼哈顿距离总和
    '''
    E_cost = 0
    for i in range(4):
        for j in range(4):
            if cur_state[i][j] == SG[i][j]:
                continue
            num = cur_state[i][j]
            if num == 0:
                x, y = 3, 3
            else:
                x = num / 4  # 理论横坐标
                y = num - 4 * x - 1  # 理论的纵坐标
                E_cost += math.sqrt((x - i)*(x - i) + (y - j)*(y - j))
    return E_cost

def generate_child(sn_node, sg_node, hash_set, open_table, cal_distence,SG):
    '''
    生成子节点函数
    :参数 sn_node:  当前节点
    :参数 sg_node:  最终状态节点
    :参数 hash_set:  哈希表，用于判重
    :参数 open_table: OPEN表
    :参数 cal_distence: 距离函数
    :返回: None
    '''
    if sn_node == sg_node:
        heapq.heappush(open_table, sg_node)
        print('已找到终止状态！')
        return
    for i in range(0, 4):
        for j in range(0, 4):
            if sn_node.state[i][j] != 0:
                continue
            for d in ['up', 'down', 'left', 'right']:  # 四个偏移方向
                x = i + MOVE[d][0]
                y = j + MOVE[d][1]
                if x < 0 or x >= 4 or y < 0 or y >= 4:  # 越界了
                    continue
                state = copy.deepcopy(sn_node.state)  # 复制父节点的状态
                state[i][j], state[x][y] = state[x][y], state[i][j]  # 交换位置
                h = hash(str(state))  # 哈希时要先转换成字符串
                if h in hash_set:  # 重复了
                    continue
                hash_set.add(h)  # 加入哈希表

                # 记录扩展节点的个数
                global SUM_NODE_NUM
                SUM_NODE_NUM += 1

                deepth = sn_node.deepth + 1  # 已经走的距离函数
                rest_dis = cal_distence(state, SG)  # 启发的距离函数
                node = State(deepth, rest_dis, state, h, sn_node)  # 新建节点
                sn_node.child.append(node)  # 加入到孩子队列
                heapq.heappush(open_table, node)  # 加入到堆中

                # show_block(state, deepth) # 打印每一步的搜索过程

def A_start(start, end, distance_fn, generate_child_fn):
    '''
    A*算法
    :参数 start: 起始状态
    :参数 end: 终止状态
    :参数 distance_fn: 距离函数，可以使用自定义的
    :参数 generate_child_fn: 产生孩子节点的函数
    :返回: 最优路径长度
    '''
    root = State(0, 0, start, hash(str(start)), None)  # 根节点
    end_state = State(0, 0, end, hash(str(end)), None)  # 最后的节点
    if root == end_state:
        print("start == end !")

    OPEN.append(root)
    heapq.heapify(OPEN)

    node_hash_set = set()  # 存储节点的哈希值
    node_hash_set.add(root.hash_value)
    while len(OPEN) != 0:
        top = heapq.heappop(OPEN)
        if top == end_state:  # 结束后直接输出路径
            return print_path(top)
        # 产生孩子节点，孩子节点加入OPEN表
        generate_child_fn(sn_node=top, sg_node=end_state, hash_set=node_hash_set,
                          open_table=OPEN, cal_distence=distance_fn)
    print("无搜索路径!")  # 没有路径
    return -1

def print_path(node):
    '''
    输出路径
    :参数 node: 最终的节点
    :返回: None
    '''
   # print("最终搜索路径为：")
    steps = node.deepth

    stack = []  # 模拟栈
    while node.father_node is not None:
        stack.append(node.state)
        node = node.father_node
    stack.append(node.state)
    step = 0
    while len(stack) != 0:
        t = stack.pop()
        show_block(t, step)
        step += 1
    return steps

def show_block(block, step):
    print("*"*10)
    for b in block:
        print(b)

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