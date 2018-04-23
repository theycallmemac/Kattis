from collections import defaultdict
import itertools
def main():

    lst = [' + ', ' - ', ' * ', ' // ']
    
    dict = defaultdict(int)

    for ops in itertools.product(lst, repeat=3):
        cmd = '4' + '4'.join(ops) + '4'
        result = eval(cmd)
        dict[result] = cmd.replace('//', '/')

    cases = int(input())
    for _ in range(cases):
        n = int(input())
        
        if n in dict:
            print(dict[n], '=', n)
        else:
            print('no solution')
if __name__ == '__main__':
    main()
