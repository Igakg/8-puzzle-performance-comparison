from sys import argv
import glob

def connectcsv():
    method = argv[1]
    files = glob.glob(f'output_{method}*.csv')

    with open(f'output_{method}_combined.csv', 'w') as outfile:
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