# 8-puzzle-performance-comparison

A tool to solve the 8-puzzle with multiple search algorithms and compare their performance.  
Runs IDS, A*(h0), A*(h1), and A*(h2) on 100 random initial states each, outputting results to CSV.

> **Original**: [abpaudel/8-puzzle](https://github.com/abpaudel/8-puzzle) (GPLv3)  
> **Modified by**: Igakg (2026)

[日本語版 README はこちら](README.ja.md)

---

## Algorithms

| Identifier | Algorithm | Heuristic |
|------------|-----------|-----------|
| `ids`  | Iterative Deepening Search (IDS) | None |
| `ast0` | A* | h(n) = 0 (equivalent to Dijkstra) |
| `ast1` | A* | h(n) = Number of misplaced tiles |
| `ast2` | A* | h(n) = Manhattan distance |

**Goal state**:
```
1 2 3
8 0 4
7 6 5
```

---

## Setup

### Requirements
- Python 3.x
- numpy

### Installation

```bash
git clone https://github.com/Igakg/8-puzzle-performance-comparison.git
cd 8-puzzle-performance-comparison
pip install numpy
```

---

## Usage

### Run with a specific initial state

```bash
python main.py <algorithm> <initial_state>
```

Example:
```bash
python main.py ids 1,2,5,3,4,0,6,7,8
python main.py ast2 1,2,5,3,4,0,6,7,8
```

### Run with random initial states

```bash
python main.py <algorithm> random [n]
```

`n` specifies the number of runs (default: 5).

Example:
```bash
python main.py ids random        # runs 5 times (default)
python main.py ast0 random 100   # runs 100 times
python main.py ast1 random 50
python main.py ast2 random 100
```

In `random` mode, only solvable states are generated. Results are written to individual CSVs for each run.

---

## Output Files

Each run produces a CSV file:

```
output_<algorithm>_<index>.csv
```

Columns:

| Column | Description |
|--------|-------------|
| `cost_of_path` | Number of moves to reach the goal |
| `nodes_expanded` | Number of nodes expanded |
| `nodes_explored` | Number of nodes explored |
| `search_depth` | Depth of the solution |
| `max_search_depth` | Maximum depth reached during search |

### Combine CSVs into one file

```bash
python connectcsv.py <algorithm>
```

Example:
```bash
python connectcsv.py ast2
```

Produces `output_ast2_combined.csv`.

---

## File Structure

```
8-puzzle-performance-comparison/
├── main.py          # Entry point & random state generation
├── board.py         # Board state, moves, and heuristics
├── solver.py        # Abstract solver base class
├── ids.py           # IDS implementation
├── astar0.py        # A*(h=0) implementation
├── astar1.py        # A*(misplaced tiles) implementation
├── astar2.py        # A*(Manhattan distance) implementation
└── connectcsv.py    # Tool to combine multiple CSVs
```

---

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).  
Original author: [abpaudel](https://github.com/abpaudel/8-puzzle)
