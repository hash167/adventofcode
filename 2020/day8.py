from copy import deepcopy


class VM:
    def __init__(self, tokens):
        self.tokens = tokens
        self.acc = 0
        self.ip = 0
        self.executed = []

    def cycle(self, terminate: bool):
        if self.ip in self.executed and terminate:
            return True, False
        self.executed.append(self.ip)
        if self.ip == len(self.tokens):
            return False, False
        inst, val = self.tokens[self.ip]
        if inst == 'acc':
            self.acc += val
            self.ip += 1
        if inst == 'nop':
            self.ip += 1
        if inst == 'jmp':
            self.ip += val
        return False, True


if __name__ == "__main__":
    with open('inputs/day8.txt') as f:
        tokens = []
        for line in f:
            inst, arg = line.strip().split(" ")
            value = int(arg[1:]) if arg[0] == "+" else -int(arg[1:]) 
            tokens.append((inst, value))
        vm = VM(tokens)
        while True:
            repeated, cont = vm.cycle(True)
            if repeated:
                break
        print(vm.acc)
    with open('inputs/day8.txt') as f:
        for count, line in enumerate(f):
            tokens_copy = deepcopy(tokens)
            cont_outer = False
            break_outer = False
            inst, arg = line.strip().split(" ")
            if inst == 'nop':
                tokens_copy[count] = ('jmp', tokens_copy[count][1])
            if inst == 'jmp':
                tokens_copy[count] = ('nop', tokens_copy[count][1])
            vm = VM(tokens_copy)
            while True:
                repeated, cont = vm.cycle(True)
                if not cont:
                    if repeated:
                        cont_outer = True
                    else:
                        break_outer = True
                    break
            if cont_outer:
                continue
            if break_outer:
                break
    print(vm.acc)
    
