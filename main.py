# ==============================================================================
# Original File: main.py
# Copyright (C) abpaudel (https://github.com/abpaudel/8-puzzle)
#
# This file is part of "8-puzzle" and is licensed under the 
# GNU General Public License v3.0 (GPLv3).
# See <https://www.gnu.org/licenses/gpl-3.0.en.html> for details.
# ==============================================================================
# Modifications
# 2026-05-27: Igakg
#   - [変更内容1: IDDFSクラスをIDSクラスにリネーム]
#   - [変更内容2: dst,bfsクラスを削除し、idsクラスとastarクラスのみを残す]
# 2026-06-02: Igakg
#   - [変更内容3: arg[2]が"random"の場合、ランダムな状態を生成するように変更、課題ではこれを用いる]
#   - [変更内容4: randomで出力する状態を逆転数の偶奇に応じて、解ける状態となるまで生成を試みるよう変更(solvable関数の追加)]
#   - [変更内容5: 出力ファイル形式をcsvに変更、cpu関連の出力を削除、ファイル名も"{alg}_output1.csv"に変更]
#   - [変更内容6: randomで生成した場合に10回生成]
#   - [変更内容7: ast0,ast1,ast2クラスをインポートするように変更、入力に応じてこれらのクラスを用いるように変更]
# 2026-06-07: Igakg
#   - [変更内容8: 第3引数でランダム実行回数を指定可能に変更、状態指定時は1回のみ実行]
# 2026-06-08: Igakg
#   - [変更内容9: ゴール状態の変更(board.py)に合わせ、solvable関数をGOALの転倒数の偶奇と比較するように修正]
# ==============================================================================

import resource
import sys

import numpy as np
from astar0 import AStar0
from astar1 import AStar1
from astar2 import AStar2
from board import Board, GOAL
from ids import IDS

def count_inversions(state):
    flat_board = [num for num in state if num != 0]

    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j]:
                inversions += 1

    return inversions

def solvable(state):
    return count_inversions(state) % 2 == count_inversions(GOAL) % 2

def main():
    alg = sys.argv[1]
    state_arg = sys.argv[2]

    if state_arg == 'random':
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    else:
        n = 1

    for i in range(n):
        if state_arg == 'random':
            while True:
                p = Board(np.random.permutation(9))
                if solvable(p.state):
                    print("generated solvable state. Now searching")
                    break
                else:
                    print("generated unsolvable state")
        else:
            p = Board(np.array(eval(state_arg)))

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