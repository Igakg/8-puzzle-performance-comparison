# Modifications
# 2026-06-10: Igakg
#   - globの結果からoutput_{method}_combined.csv自身を除外し、再実行時の自己参照を防止
from sys import argv
import glob

def connectcsv():
    method = argv[1]
    combined_name = f'output_{method}_combined.csv'
    files = [f for f in glob.glob(f'output_{method}*.csv') if f != combined_name]

    with open(combined_name, 'w') as outfile:
        outfile.write('cost_of_path,nodes_expanded,nodes_explored,search_depth,max_search_depth\n')
        for fname in files:
            with open(fname) as infile:
                header = infile.readline()
                if not header:
                    continue  # 空ファイルならスキップ
                for line in infile:
                    outfile.write(line)
            outfile.write('\n')

if __name__ == "__main__":
    connectcsv()