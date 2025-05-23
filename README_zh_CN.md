```markdown
# 🧩 15 个使用 A* 算法的谜题求解器

该项目实现了 **A\***（A-star）搜索算法来解决经典的 **15 块拼图**（滑动拼图）。它使用可接受的启发式算法（曼哈顿距离）来有效地找到最优解。

---

## 📌 什么是 15 拼图？

15 拼图是一个 4x4 的网格，包含 15 个编号的方块和一个空白处。目标是将方块按正确的顺序滑动：

```
 1  2  3  4  
 5  6  7  8  
 9 10 11 12  
13 14 15  _  
```

您可以将相邻的方块移动到空白处。

---

## 🚀 功能

- ✅ 使用曼哈顿距离启发式算法的 A* 搜索
- ✅ 在尝试解决之前进行可解性检查
- ✅ 逐步路径输出
- ✅ 显示总移动次数、所用时间和扩展节点
- 🔧 轻松扩展到其他启发式方法

---

## 📂 项目结构

```
A-star-method/
├── utils/                         # 有用的工具
│   ├── Classes.py
│   └── Functions.py
├── Comprehesive.py                # 简单运行脚本
├── EightDigits.py                 # 8块拼图简化版本
├── FifteenDigits_Best.py          # 最优操作版本
├── FifteenDigits_Initial.py       # 初始操作版本
├── ListMethodsCustomize.py        # 定制目标和初始状态
├── README.md                      # 英文介绍
└── README_zh_CN.md                # 本文件
```

---

## 🧠 启发式函数

曼哈顿距离启发式方法是每个图块与其目标位置的距离之和：

```
h(n) = Σ |current_row - goal_row| + |current_col - goal_col|
```

它是 **可接受的** 并且能确保最佳解决方案。

---

## 🛠️ 如何运行

1. 克隆存储库：

```bash
git clone https://github.com/Steven1Yang/A-star-method.git
cd A-star-method
```

2. 运行程序：

```bash
python xxx.py          # 用具体脚本名替换 xxx
```

3. 输入初始状态（用 `0` 表示空白处）：

```
Enter the initial state (e.g. '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0'):
```

---

## ✅ 示例

```
输入:
1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0

输出:
Puzzle is solvable.
Solving...
Moves required: 2
Path: Left → Left
Nodes expanded: 14
Time taken: 0.021s
```

---

## 🧪 待办事项

- [ ] 添加更多启发式方法（例如线性冲突）
- [ ] GUI 可视化
- [ ] 与 IDA* 性能比较

---
