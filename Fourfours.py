# four 4's
# operations +,-,*,/    ,sqrt,exp

import math

ops2 = {}
ops2["+"] = lambda x,y : x+y
ops2["-"] = lambda x,y : x-y
ops2["*"] = lambda x,y : x*y
ops2["/"] = lambda x,y : x/y

# memo = {}

def check_eqn(eqn):
    mid = len(eqn) // 2
    op = eqn[mid]
    x = int(eqn[:mid])
    y = int(eqn[mid+1:])
    return ops2[op](x,y)

num = 1
total = 3
nums_left = 2

while nums_left > 0:
    for op in ops2.keys():
        eqn = str(num)+op+str(num)
        if check_eqn(eqn) == total:
            nums_left -= 2
            break
    nums_left = -1
    print(eqn)






















class FourFours:

    ops2 = {}
    ops2["+"] = lambda x,y : x+y
    ops2["-"] = lambda x,y : x-y

    # takes an int and returns the equation of with 4 4s using operations as a string
    @staticmethod
    def get_equation(x,y):
        return FourFours.ops["+"](x,y)


class Operation:

    def __init__(name, func):
        self.name = name
        self.func = func

    def eval(operands):

        return self.func(operands)




# print(FourFours.get_equation(1,2))


# print_four_fours(list of ops)

# print(math.pow())
