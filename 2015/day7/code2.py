from typing import Dict

def solve(a, b, op):
    if b is None and op == 'NOT':
        return int((~a) & 0xFFFF)
    if op == 'AND':
        return int(a & b)
    elif op == 'OR':
        return int(a | b)
    elif op == 'LSHIFT':
        return int((a << b) & 0xFFFF)
    elif op == 'RSHIFT':
        return int(a >> b)


def main():
    expressions: Dict[str, str] = {}
    memo: Dict[str, int] = {}

    with open('input.txt', 'r') as file:
        for line in file:
            # print(line.strip())
            exp, var = line.strip().split(' -> ')
            expressions[var] = exp

    def recur(var):
        if var in memo:
            return memo[var]
        else:
            res = None
            exp = expressions[var]
            parts = exp.split()
            if len(parts) == 3:
                a = int(parts[0]) if parts[0].isdigit() else recur(parts[0]) 
                b = int(parts[2]) if parts[2].isdigit() else recur(parts[2]) 
                res = solve(a, b, parts[1])
            elif len(parts) == 2:
                a = int(parts[1]) if parts[1].isdigit() else recur(parts[1]) 
                res = solve(a, None, parts[0])
            elif len(parts) == 1:
                res = int(parts[0]) if parts[0].isdigit() else int(recur(parts[0]))
            
            if res is None:
                raise ValueError("WHAT THE HECKKKKK")
           
            memo[var] = res
            return res
    
    for var in expressions:
        recur(var)

    prev_a = memo['a']
    memo = {}
    memo['b'] = prev_a

    for var in expressions:
        recur(var)
    
    print(memo['a'])



if __name__ == "__main__":
    main()