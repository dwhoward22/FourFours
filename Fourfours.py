import math

# class Partition:
#     def __init__(self, p0, p1, depth=0):
#         self.p0 = p0
#         self.p1 = p1
#         self.depth = depth
#         self.is_pair = False
#         if len(p0) == 1 and len(p1) == 1:
#             self.is_pair = True
#
#     def get_pair(self):
#         return [self.p0[0], self.p1[0]] if self.is_pair else [self.p0, self.p1]
#
#     def make_pairs(self):
#         pass

class InvalidExprError(Exception):
    pass

class Expression:
    def __init__(self, expression):
        # can maybe add check for type
        if not expression:
            raise InvalidExprError
        self.A = expression
        self.val = None

    def __str__(self):
        return str(self.A)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def eval(self):
        if self.val is None:
            self.val = self.A.eval()
        return self.val

    def num_fours(self):
        return self.A.num_fours()

class Binary(Expression):
    def __init__(self, A, B):
        if not B:
            raise InvalidExprError
        self.A = A
        self.B = B
        self.val = None
        self.num_four = self.A.num_fours() + self.B.num_fours()

    def num_fours(self):
        return self.num_four

# This inheretance may be a problem in the future?
class Int(Expression):
    def __str__(self):
        return str(self.A)

    def eval(self):
        return self.A

    def num_fours(self):
        return 1

class Add(Binary):
    def __str__(self):
        return "(" + str(self.A) + " + " + str(self.B) + ")"

    def eval(self):
        if self.val is None:
            self.val = self.A.eval() + self.B.eval()
        return self.val

class Sub(Binary):
    def __str__(self):
        return "(" + str(self.A) + " - " + str(self.B) + ")"

    def eval(self):
        if self.val is None:
            self.val = self.A.eval() - self.B.eval()
        return self.val

class Mul(Binary):
    def __str__(self):
        return "(" + str(self.A) + " * " + str(self.B) + ")"

    def eval(self):
        if self.val is None:
            self.val = self.A.eval() * self.B.eval()
        return self.val

class Div(Binary):
    def __init__(self, A, B):
        if B.eval() == 0:
            raise InvalidExprError
        super().__init__(A, B)

    def __str__(self):
        return "(" + str(self.A) + " / " + str(self.B) + ")"

    def eval(self):
        if self.val is None:
            try:
                self.val = self.A.eval() / self.B.eval()
            except:
                raise InvalidExprError
        return self.val

class Exp(Binary):
    def __init__(self, A, B):
        if B.eval() > 10 or A.eval() > 10 or (A.eval() == 0 and B.eval() <= 0) or (A.eval() < 0 and math.floor(B.eval()) != B.eval()):
            raise InvalidExprError
        super().__init__(A, B)

    def __str__(self):
        return "(" + str(self.A) + " ^ " + str(self.B) + ")"

    def eval(self):
        if self.val is None:
            self.val = self.A.eval() ** self.B.eval()
        return self.val

class Sqrt(Expression):
    def __init__(self, A):
        if A.eval() < 0:
            raise InvalidExprError
        super().__init__(A)

    def __str__(self):
        return "√" + str(self.A)

    def eval(self):
        if self.val is None:
            self.val = self.A.eval() ** 0.5
        return self.val

class Fact(Expression):
    def __init__(self, A):
        if A.eval() < 0 or A.eval() > 10 or math.floor(A.eval()) != A.eval():
            raise InvalidExprError
        super().__init__(A)

    def __str__(self):
        return str(self.A) + "!"

    def eval(self):
        if self.A.eval() < 0:
            raise InvalidExprError
        if self.val is None:
            self.val = self.factorial(self.A.eval())
        return self.val

    def factorial(self, n):
        if n in [0,1]:
            return 1
        else:
            return n * self.factorial(n-1)

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
fours_exp_table = {}
bin_exps = [Add, Sub, Mul, Div, Exp]
una_exps = [Sqrt, Fact]
found_vals = {4}
found_fours_vals = set()

# Using 3 fours
iters = 6
for i in range(iters):
    curr_exps = list(exp_table.keys())
    for exp in bin_exps:
        for i in curr_exps:
            if i.num_fours() >= 4:
                continue
            for j in curr_exps:
                if j.num_fours() >= 4 or i.num_fours() + j.num_fours() > 4:
                    continue
                # Make expression
                try:
                    exp1 = exp(i, j)
                except InvalidExprError:
                    continue
                try:
                    val = exp1.eval()
                except OverflowError:
                    print(exp1)
                if exp1.num_fours() == 4 and val not in found_fours_vals:
                    found_fours_vals.add(val)
                    fours_exp_table[exp1] = val
                if val not in found_vals:
                    found_vals.add(val)
                    exp_table[exp1] = val

    for exp in una_exps:
        for i in curr_exps:
            if i.num_fours() > 4:
                continue
            try:
                exp1 = exp(i)
            except InvalidExprError:
                continue
            val = exp1.eval()
            if exp1.num_fours() == 4 and val not in found_fours_vals:
                found_fours_vals.add(val)
                fours_exp_table[exp1] = val
            if val not in found_vals:
                found_vals.add(val)
                exp_table[exp1] = val


ordered = []
for k, v in fours_exp_table.items():
    # ordered.append((v, f"{k} = {v}"))
    ordered.append((v, f"{v} = {k}"))
ordered.sort(key=lambda x:x[0])

print_all = False
for i in ordered:
    if not print_all:
        if i[0] < 0 or i[0] != int(i[0]):
            continue
    print(i[1])






# for exp1 in exps:
#     for exp2 in exps:
#         exp1 = exp1(four, four)
#         exp2 = exp2(four, four)
#
#         expressions.append()
