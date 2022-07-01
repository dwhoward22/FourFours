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

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__str__() == other.__str__()

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
        return "(" + str(self.A) + " * " + str(self.B) + ")"

class Div(Binary):
    # raise error in __init__ when making expression save time
    def eval(self):
        if self.val is None:
            try:
                self.val = self.A.eval() / self.B.eval()
            except:
                raise InvalidExprError
        return self.val

    def __str__(self):
        return "(" + str(self.A) + " / " + str(self.B) + ")"

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
    # raise error in __init__ when making expression save time
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




four = Int(4)

# three = Int(3)
# mul = Mul(four, three)
# exp = Sub(mul, mul)
# print(exp.eval())


expressions = []
# for exp in [Add, Div]:
#     expressions.append(exp(four, four))
#
# for e in expressions:
#     print(f"{e} = {e.eval()}")



exp_table = {Int(4):4}
exps = [Add, Sub, Mul, Div]

# Using 3 fours
iters = 1
for i in range(iters):
    curr_exps = list(exp_table.keys())
    for exp in exps:
        for i in curr_exps:
            for j in curr_exps:
                exp = exp(i, j)
                exp_table[exp] = exp.eval()







# for exp1 in exps:
#     for exp2 in exps:
#         exp1 = exp1(four, four)
#         exp2 = exp2(four, four)
#
#         expressions.append()
