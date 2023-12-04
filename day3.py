# f = open('day3input.txt', 'r')
f = open('day3sample.txt', 'r')
paths = f.readlines()

# sets!

w1 = set()
w2 = set()

# Part 1
path1 = paths[0].strip().split(',')
path2 = paths[1].strip().split(',')

def set_paths(path, wire):
    x, y = 0, 0
    for instr in path:
        dir = instr[0]
        num = int(instr[1:])
        if dir == 'R':
            for i in range(num):
                x += 1
                wire.add((x,y))
        elif dir == 'L':
            for i in range(num):
                x -= 1
                wire.add((x,y))
        elif dir == 'U':
            for i in range(num):
                y += 1
                wire.add((x,y))
        elif dir == 'D':
            for i in range(num):
                y -= 1
                wire.add((x,y))
    return wire

set_paths(path1, w1)
# set_paths(path2, w2)

# min_dist = float('inf')
# for coord in w1.intersection(w2):
#     dist = abs(coord[0]) + abs(coord[1])
#     if dist < min_dist:
#         min_dist = dist

# print(min_dist)

# Part 2


x, y = 0, 0
for instr in path2:
    dir = instr[0]
    num = int(instr[1:])
    if dir == 'R':
        for i in range(num):
            x += 1
            w2.add((x,y))
            if w1.intersection(w2):
                print(w1.intersection(w2))
    elif dir == 'L':
        for i in range(num):
            x -= 1
            w2.add((x,y))
            if w1.intersection(w2):
                print(w1.intersection(w2))
    elif dir == 'U':
        for i in range(num):
            y += 1
            w2.add((x,y))
            if w1.intersection(w2):
                print(w1.intersection(w2))
    elif dir == 'D':
        for i in range(num):
            y -= 1
            w2.add((x,y))
            if w1.intersection(w2):
                print(w1.intersection(w2))



