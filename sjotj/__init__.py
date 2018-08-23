import ast
import json
import sys
from jproperties import Properties

def read_in():
    p = Properties()
    p.load(sys.stdin)
    return p

def list_to_dict(tol,d):
        for item in tol:
            if isinstance(item[1],list):
                item[1] = list_to_dict(item[1],{})
            d[item[0]] = item[1]
        return d

def main():
    save = {}
    p = read_in()
    for k,v in p.items(): 
        st = {}
        ret = list_to_dict(ast.literal_eval(v),st)
        save[k] = ret
    print(json.dumps(save,indent=2))


if __name__ == '__main__':
    try: main()
    except: raise
