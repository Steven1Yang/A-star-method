import time
import argparse
from utils.Functions import cal_M_distence
from utils.Functions import cal_E_distence
from utils.Functions import A_start
from utils.Functions import generate_child
# 初始状态
S0 = [[11, 9, 4, 15],[1, 3, 0, 12],[7, 5, 8, 6],[13, 2, 10, 14]]

# 目标状态
SG = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 0]]

# 节点的总数
SUM_NODE_NUM = 0

if __name__ == '__main__':

    # 可配置式运行文件
    parser = argparse.ArgumentParser(description='选择距离计算方法')
    parser.add_argument('--method', '-m', help='method 选择距离计算方法(cal_E_distence or cal_M_distence)', default = 'cal_M_distence')
    args = parser.parse_args()
    method = args.method

    time1 = time.time()
    if method == 'cal_E_distence':
        length = A_start(S0, SG, cal_E_distence, generate_child)
    else:
        length = A_start(S0, SG, cal_M_distence, generate_child)
    time2 = time.time()
    if length != -1:
        #if method == 'cal_E_distence':
            #print("采用欧式距离计算启发函数")
        #else:
           # print("采用曼哈顿距离计算启发函数")
        print("探索深度", length)
        #print("搜索时长为", (time2 - time1), "s")
        print("搜索时间", SUM_NODE_NUM)

