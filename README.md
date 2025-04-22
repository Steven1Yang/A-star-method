# 🧩 15 Puzzle Solver with A* Algorithm

This project implements the **A\*** (A-star) search algorithm to solve the classic **15-puzzle** (sliding tile puzzle). It uses an admissible heuristic (Manhattan distance) to find the optimal solution efficiently.

---

## 📌 What is the 15-Puzzle?

The 15-puzzle is a 4x4 grid containing 15 numbered tiles and one empty space. The objective is to slide the tiles into the correct order:

```
 1  2  3  4  
 5  6  7  8  
 9 10 11 12  
13 14 15  _  
```

You can move adjacent tiles into the blank space.

---

## 🚀 Features

- ✅ A* Search with **Manhattan Distance** heuristic
- ✅ Solvability check before attempting to solve
- ✅ Step-by-step path output
- ✅ Shows total moves, time taken, and nodes expanded
- 🔧 Easily extendable to other heuristics

---

## 📂 Project Structure

```
A-star-method/
├── utils/                         # Useful Tools
│   ├── Classes.py
│   └── Functions.py
├── Comprehesive.py                # Simple Run
├── EightDigits.py                 # Simplified For EightDigits
├── FifteenDigits_Best.py          # Best Operation
├── FifteenDigits_Initial.py       # First Operation
├── ListMethodsCustomize.py        # Customize The Target and The Initial
├── README.md                      # This file
└── README_zh_CN.md                # Mandarin Version of README
```

---

## 🧠 Heuristic Function

The **Manhattan Distance** heuristic is the sum of the distances each tile is from its goal position:

```
h(n) = Σ |current_row - goal_row| + |current_col - goal_col|
```

It is **admissible** and ensures optimal solutions.

---

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Steven1Yang/A-star-method.git
cd A-star-method
```

2. Run the program:

```bash
python xxx.py          # Replace xxx With The Specific Script Name
```

3. Enter the initial state (use `0` for the blank):

```
Enter the initial state (e.g. '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0'):
```

---

## ✅ Example

```
Input:
1 2 3 4 5 6 7 8 9 10 11 12 13 15 14 0

Output:
Puzzle is solvable.
Solving...
Moves required: 2
Path: Left → Left
Nodes expanded: 14
Time taken: 0.021s
```

---

## 🧪 To Do

- [ ] Add more heuristics (e.g., linear conflict)
- [ ] GUI visualization
- [ ] Compare with IDA* performance

---

