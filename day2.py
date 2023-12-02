f = open('day2input.txt', 'r')
original = open('day2original.txt', 'r')
# f = open('day2sample.txt', 'r')
original_file = original.read().split(',')
codes = f.read().split(',')

original_codes = [int(_) for _ in original_file]
codes = [int(_) for _ in codes]

# Part 1

for i in range(len(codes)):
    if i % 4 == 0:
        if int(codes[i]) == 1:
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        elif codes[i] == 2:
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        elif codes[i] == 99:
            break
print(codes[0]) # 5866714

# Part 2
for noun in range(100):
    for verb in range(100):
        codes = original_codes.copy()
        codes[1] = noun
        codes[2] = verb
        for i in range(len(codes)):
            if i % 4 == 0:
                if int(codes[i]) == 1:
                    codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
                elif codes[i] == 2:
                    codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
                elif codes[i] == 99:
                    break
        output = codes[0]
        if output == 19690720:
            print(noun, verb)
            break