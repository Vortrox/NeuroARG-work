#!usr/bin/env python

import sys

TABLE_CRAZY = (
    (1, 0, 0),
    (1, 0, 2),
    (2, 2, 1)
)

ENCRYPT = list(map(ord,
              '5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB'\
              '6v^=I_0/8|jsb9m<.TVac`uY*MK\'X~xDl}REokN:#?G\"i@'))

OPS_VALID = (4, 5, 23, 39, 40, 62, 68, 81)

POW9, POW10 = 3**9, 3**10

# --------------------------------------------------

def rotate(n):
    return POW9*(n%3) + n/3

def crazy(a, b):
    result = 0
    d = 1

    for i in range(10):
        result += TABLE_CRAZY[int((b/d)%3)][int((a/d)%3)] * d
        d *= 3

    return result

def initialize(source, mem):
    i = 0

    for c in source:
        if c == ' ' or c == '\n':
            continue

        # if (ord(c)+i) % 94 not in OPS_VALID:
        #     print('Invalid character in the source file')
        #     sys.exit(1)

        if i == POW10:
            print('Source file is too long')
            sys.exit(1)

        mem[i] = ord(c)
        i += 1

    while i < POW10:
        mem[i] = crazy(mem[i-1], mem[i-2])
        i += 1

def interpret(mem):
    write = sys.stdout.write
    flush = sys.stdout.flush
    read = sys.stdin.read
    instructions = []
    memory_state = []
    read_address = set()
    a, c, d = 0, 0, 0
    counter = 0
    # mem.is_enabled = False
    while 1:
        mem.toggle()
        # memory_state.append("".join(chr(int(data % 256)) for data in mem)[:1000])
        counter += 1
        if mem[c] < 33 or mem[c] > 126:
            return

        v = (mem[c]+c) % 94

        if v == 4:                        # jmp [d]
            c = mem[d]
            instructions.append(f"jmp [{d}]")
        elif v == 5:                      # out a
            character = chr(int(a % 256))
            instructions.append(f"out {character}")
            write(character)
            flush()
        elif v == 23:                     # in a
            a = ord(read(1))
            instructions.append(f"in {a}")
        elif v == 39:                     # rotr[d]; mov a, [d]
            instructions.append(f"rotr[{d}]; mov {a}, [{d}]")
            a = mem[d] = rotate(mem[d])
        elif v == 40:                     # mov d, [d]
            instructions.append(f"mov {d}, [{d}]")
            d = mem[d]
        elif v == 62:                     # crz [d], a; mov a, [d]
            instructions.append(f"crz [{d}]; {a}; mov {a}, [{d}]")
            a = mem[d] = crazy(a, mem[d])
        # elif v == 68:                   # nop
        #     pass
        elif v == 81:                     # end
            instructions.append("end")
            print()
            print(*instructions, sep="\n")
            return
        else:
            pass

        mem.toggle()

        if mem[c] >= 33 and mem[c] <= 126:
            mem[c] = ENCRYPT[mem[c] - 33]

        c = 0 if c == POW10-1 else c+1
        d = 0 if d == POW10-1 else d+1

# --------------------------------------------------

class CustomMemory:
    def __init__(self, memory):
        self.memory = memory
        self.addr_written_to = set()
        self.addr_read_from = set()
        self.is_enabled = True

    def __getitem__(self, key):
        if self.is_enabled:
            self.addr_read_from.add(key)
        return self.memory[key]

    def __setitem__(self, key, value):
        if self.is_enabled:
            self.addr_written_to.add(value)
        self.memory[key] = value

    def toggle(self):
        return
        self.is_enabled = not self.is_enabled

if __name__ == '__main__':
    filename = "input_malbolge.txt"

    try:
        with open(filename, 'r') as p:
            source = p.read()
    except IOError:
        print('Unable to open the file')
        sys.exit(1)


    mem = CustomMemory([0] * POW10)
    initialize(source, mem)

    # experiment: modify bytes 3-39
    # print("".join(chr(mem[i]) for i in range(len(source))))
    # for i in range(3, 40):
    #     mem[i] = 68
    # print("".join(chr(mem[i]) for i in range(len(source))))

    try:
        mem.addr_written_to = set()
        mem.addr_read_from = set()
        interpret(mem)

        from copy import copy
        read_copy = copy(mem.addr_read_from)
        write_copy = copy(mem.addr_written_to)
        unread = [i for i in range(len(source)) if i not in read_copy]
        unwritten = [i for i in range(len(source)) if i not in write_copy]
        print("".join(source[c] for c in unread))
        code = "".join(source[c] for c in unread)
        new_mem = CustomMemory([0] * POW10)
        initialize(code, new_mem)
        interpret(new_mem)
    except KeyboardInterrupt:
        print('\nUser interrupt')
        sys.exit(0)

    pass