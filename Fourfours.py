import math
from abc import ABC


class Fours_Solver:

    fours = [4,4,4,4]
    functions = ["Add", "Sub", "Mul", "Div", "Exp", "Sqrt", "Fact"]
    max_depth = 3 # How many times can self partition for nested function

    op_val_dict = {} # OR this one if we hash on A and B maybe __repr__
    val_exp_dict = {} # THIS IS BIG can be used as memo in make_pairs/expr

    def __init__(self):
        partitions = self.get_partitions(self.fours)
        for p in partitions:
            for funct in self.functions:
                pairs = self.make_pairs(p)
                for pair in pairs:
                    try:
                        expr = make_expr(pair, funct)
                        val_exp_dict[expr.eval()] = expr
                    except InvalidExprError:
                        continue




    """
    Returns list of 2-partitions of x
    """
    def get_partitions(self, x, depth=0):
        parts = []
        # parts.append([x]) # add partition of only whole list
        for i in range(1,len(x)+1):
            p0 = x[:i]
            p1 = x[i:]
            if len(p0) == 0 or len(p1) == 0:
                depth = depth + 1
            p = Partition(x[:i], x[i:], depth)
            parts.append(p)
        return parts

    def make_pairs(self, part):
        if part.is_pair:
            return part.get_pair(part)
        pairs = []
        firsts = []
        if len(part.p0) > 1:
            firsts = self.get_partitions(part.p0, part.depth + 1)
        for f in firsts:

    def make_expressions(self, part):
        out = []
        if part.depth >= max_depth:
            pass
        else:
            parts_0 = []
            parts_1 = []
            if len(part.p0) > 0:
                parts_0 = self.get_partitions(part.p0, part.depth)
            if len(part.p1) > 0:
                parts_1 = self.get_partitions(part.p1, part.depth)
            expr_0 = []
            expr_1 = []
            for p0 in parts_0:
                expr_0.extend(make_expressions(p0))
            for p1 in parts_1:
                expr_1.extend(make_expressions(p1))
            for e0 in expr_0:
                for e1 in expr_1:
                    for op in self.functions:
                        out.append(self.make_expr([e0, e1], ))



    def make_expr(self, pair, f):
        expr = None
        p0 = pair[0]
        p1 = pair[1]
        if f == "Add":
            expr = Add(p0, p1)
        elif f == "Sub":
            expr = Sub(p0, p1)
        elif f == "Mul":
            expr = Mul(p0, p1)
        elif f == "Div":
            expr = Div(p0, p1)
        elif f == "Exp":
            expr = Exp(p0, p1)
        elif f == "Sqrt":
            expr = Sqrt(p0, p1)
        elif f == "Fact":
            expr = Fact(p0, p1)
        return expr



    """
    Finds the expression of 4's and operations which equals n
    """
    def find_equation(self, n):
        eqn = val_exp_dict.get(n, None)

        partitions = get_partitions(self.fours)
        for p in partitions:
            for funct in self.functions:
                if op.operands() != len(p):
                    continue
                self.eval(op, p)

    def recurse_find_values(self, x):
        vals = []
        partitions = get_partitions(x)
        for p in partitions:
            for op in self.operators:
                if op.operands() != len(p):
                    continue
                self.eval(op, p)

    def get_simple_parts(self, p):
        out = []
        for pi in p:
            if len(pi) > 1:
                vals = self.recurse_find_values(x)

    def eval(self, op, part):
        evals = []
        ps = get_simple_parts(part)
        for p in ps:
            evals.append(op.eval(p))

# Need to return some type which holds value and operations to get to value


    class Partition:
        def __init__(self, p0, p1, depth=0):
            self.p0 = p0
            self.p1 = p1
            self.depth = depth
            self.is_pair = False
            if len(p0) == 1 and len(p1) == 1:
                self.is_pair = True

        def get_pair(self):
            return [self.p0[0], self.p1[0]] if self.is_pair else [self.p0, self.p1]

        def make_pairs(self):
            pass

    class InvalidExprError(Exception):
        pass

    class Expression:
        def __init__(self, expression):
            if not expression:
                raise InvalidExprError
            self.A = expression
            self.val = None

        def eval(self):
            if self.val is None:
                self.val = self.A.eval()
            return self.val

        def __str__(self):
            return str(self.A)

    class Binary(Expression):
        def __init__(self, A, B):
            if not B:
                raise InvalidExprError
            self.A = A
            self.B = B
            self.val = None

    class Int(Expression):
        def eval(self):
            return self.A

        def __str__(self):
            return str(self.A)

    class Add(Binary):
        def eval(self):
            if self.val is None:
                self.val = self.A.eval() + self.B.eval()
            return self.val

        def __str__(self):
            return "(" + str(self.A) + " + " + str(self.B) + ")"

    class Sub(Binary):
        def eval(self):
            if self.val is None:
                self.val = self.A.eval() - self.B.eval()
            return self.val

        def __str__(self):
            return "(" + str(self.A) + " - " + str(self.B) + ")"

    class Mul(Binary):
        def eval(self):
            if self.val is None:
                self.val = self.A.eval() * self.B.eval()
            return self.val

        def __str__(self):
            return "(" + str(self.A) + " / " + str(self.B) + ")"

    class Div(Binary):
        def eval(self):
            if self.val is None:
                try:
                    self.val = self.A.eval() / self.B.eval()
                except:
                    raise InvalidExprError
            return self.val

        def __str__(self):
            return "(" + str(self.A) + " * " + str(self.B) + ")"

    class Exp(Binary):
        def eval(self):
            if self.val is None:
                self.val = self.A.eval() ** self.B.eval()
            return self.val

        def __str__(self):
            return "(" + str(self.A) + " ^ " + str(self.B) + ")"

    class Sqrt(Expression):
        def eval(self):
            if self.val is None:
                self.val = self.A.eval() ** 0.5
            return self.val

        def __str__(self):
            return "√" + str(self.A)

    class Fact(Expression):
        def eval(self):
            if self.A.eval() < 0:
                raise InvalidExprError
            if self.val is None:
                self.val = factorial(self.A.eval())
            return self.val

        def factorial(n):
            if n in [0,1]:
                return 1
            else:
                return n * factorial(n-1)

        def __str__(self):
            return str(self.A) + "!"

    class Floor(Expression):
        pass

    class Ceil(Expression):
        pass



if __name__ == '__main__':
    # solver = Fours_Solver()
    str = "str"
    print(str[0], str[0:])
    print("√"+"4")
