from abc import ABC, abstractmethod
import itertools


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


class Expression(ABC):
    @abstractmethod
    def evaluate(self):
        pass


class Number(Expression):
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f'Num value: {self.value}'

    def evaluate(self, partB=False):
        return self.value


class InfixExpression(Expression):
    def __init__(self):
        self.operands = []
        self.operators = []

    def __repr__(self):
        return f'{self.operators} - {self.operands}'

    def evaluate(self, partB=False):
        if not partB:
            result = self.operands[0].evaluate()
            for i in range(1, len(self.operands)):
                result = self.operators[i - 1](result, self.operands[i].evaluate())
        else:
            result = 1
            i = 1
            while i < len(self.operands):
                if self.operators[i - 1](1, 1) == 2:
                    prev_val = self.operands[i - 1].evaluate(True)
                    curr_val = self.operands[i].evaluate(True)
                    self.operands = list(itertools.chain(self.operands[0: i], 
                                         self.operands[i + 1: len(self.operands)]))
                    self.operands[i - 1] = Number(prev_val + curr_val)
                    self.operators = list(itertools.chain(self.operators[0: i - 1],
                                          self.operators[i: len(self.operators)]))
                    continue
                
                i += 1
            for i in range(len(self.operands)):
                result *= self.operands[i].evaluate(True)

        return result


if __name__ == "__main__":
    with open('inputs/day18.txt') as f:
        all_expr = []
        for i, line in enumerate(f):
            tokens = line.strip().replace('(', '( ').replace(')', ' )').split(' ')
            curr = InfixExpression()
            curr_expr = [curr]
            for i, token in enumerate(tokens):
                peek = curr_expr[-1]
                if token == "(":
                    child = InfixExpression()
                    peek.operands.append(child)
                    curr_expr.append(child)
                elif token == ")":
                    curr_expr = curr_expr[:-1]
                elif token == "+":
                    peek.operators.append(add)
                elif token == '*':
                    peek.operators.append(mul)
                else:
                    peek.operands.append(Number(int(token)))
            all_expr.append(curr)
        res = 0
        for expr in all_expr:
            val = expr.evaluate()
            # print(val)
            res += val
        print(res)
        res2 = 0
        for expr in all_expr:
            val = expr.evaluate(partB=True)
            # print(val)
            res2 += val
    
    print(res2)
