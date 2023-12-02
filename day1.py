f = open('day1input.txt', 'r')
# f = open('day1sample.txt', 'r')
lines = f.readlines()

# Part 1
fuel = 0
for line in lines:
    fuel += int(line) // 3 - 2

print(fuel) # part 1 solution 3502510

# Part 2
total_fuel = 0
for line in lines:
    fuel = int(line) // 3 - 2
    total_fuel += fuel
    
    while fuel > 0:
        fuel = fuel // 3 - 2
        if fuel > 0:
            total_fuel += fuel

print(total_fuel)
