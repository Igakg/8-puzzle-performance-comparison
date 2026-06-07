# ==============================================================================
# Original File: main.py
# Copyright (C) abpaudel (https://github.com/abpaudel/8-puzzle)
#
# This file is part of "8-puzzle" and is licensed under the 
# GNU General Public License v3.0 (GPLv3).
# See <https://www.gnu.org/licenses/gpl-3.0.en.html> for details.
# ==============================================================================
# Modifications
# 2026-05-27: 朝日謙伍
#   - [変更内容1: IDDFSクラスをIDSクラスにリネーム]
#   - [変更内容2: dst,bfsクラスを削除し、idsクラスとastarクラスのみを残す]
# 2026-06-02: 朝日謙伍
#   - [変更内容3: arg[2]が"random"の場合、ランダムな状態を生成するように変更、課題ではこれを用いる]
#   - [変更内容4: randomで出力する状態を逆転数の偶奇に応じて、解ける状態となるまで生成を試みるよう変更(solvable関数の追加)]
#   - [変更内容5: 出力ファイル形式をcsvに変更、cpu関連の出力を削除、ファイル名も"{alg}_output1.csv"に変更]
#   - [変更内容6: randomで生成した場合に10回生成]
#   - [変更内容7: ast0,ast1,ast2クラスをインポートするように変更、入力に応じてこれらのクラスを用いるように変更]
# ==============================================================================
"""
How to run:
$ python main.py ids 1,2,5,3,4,0,6,7,8
$ python main.py ast 1,2,5,3,4,0,6,7,8
$ python main.py ids random
$ python main.py ast0 random
$ python main.py ast1 random
$ python main.py ast2 random
"""
import resource
import sys

import numpy as np
from astar0 import AStar0
from astar1 import AStar1
from astar2 import AStar2
from board import Board
from ids import IDS

def solvable(state):
    
    flat_board = [num for num in state if num != 0]
    
    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j]:
            	inversions += 1
                
    return inversions % 2 == 0

def main():
    for i in range(100):
        if sys.argv[2] == 'random':
            while True:
                p = Board(np.random.permutation(9))
                if solvable(p.state):
                    print("generated solvable state. Now searching")
                    break
                else:
                    print("generated unsolvable state")
        else:
            p = Board(np.array(eval(sys.argv[2])))
        alg = sys.argv[1]
        if alg == 'ids':
            s = IDS(p)
        elif alg == 'ast0':
            s = AStar0(p)
        elif alg == 'ast1':
            s = AStar1(p)
        elif alg == 'ast2':
            s = AStar2(p)
        else:
            print("Invalid input, continuing through A*(2)")
            s = AStar2(p)
        s.solve()

        file = open(f'output_{alg}_{i}.csv', 'w')
        file.write('cost_of_path,nodes_expanded,nodes_explored,search_depth,max_search_depth\n')
        file.write(f"{len(s.path)},{s.nodes_expanded},{len(s.explored_nodes)},{s.solution.depth},{s.max_depth}")
        file.close()


if __name__ == "__main__":
    main()