
class Superstack():
    # <your code here>
    def __init__(self):
        self.stack = []

    def __str__(self):
        if len(self.stack) == 0:
            return 'Empty'
        else:
            return self.stack[-1]

    def push(self, v):
        """add v at top of stack"""
        self.stack.append(v)
        return self.__str__()

    def pop(self):
        """extract top element from stack"""
        if len(self.stack) > 0:
            self.stack.pop()
        return self.__str__()

    def inc(self, i, v):
        """add v to the bottom i-th element of the stack"""
        for idx in range(i):
            self.stack[idx] += v
        return self.__str__()

    def run(self, ops):
        for op in ops:
            instr = op.split()
            if instr[0] not in ('push', 'pop', 'inc'):
                print(op, "is not a valid operation. ABORT")
                return
            # Treat POP first (no arguments)
            if instr[0] == 'pop':
                print(op, ':', self.pop())
                continue
            # Then PUSH (one argument)
            try:
                value1 = int(instr[1])
            except:
                print(op, "is not a valid operation(", instr[1],"not an integer). ABORT")
                return
            if instr[0] == 'push':
                print(op, ':', self.push(value1))
                continue
            # Finally INC (two arguments)
            try:
                value2 = int(instr[2])
            except:
                print(op, "is not a valid operation(", instr[2],"not an integer). ABORT")
                return
            if instr[0] == 'inc':
                if not (0 < value1 <= len(self.stack)):
                    print(op, "is not a valid operation(", instr[1],"outside boundaries). ABORT")
                    return
                print(op, ':', self.inc(value1, value2))
        return

def main():
    operations = ['push 4', 'push 5', 'inc 2 1', 'pop', 'pop']
    stack1 = Superstack()
    stack1.run(operations)

if __name__ == "__main__":
    main()
