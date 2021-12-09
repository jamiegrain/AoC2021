f = open('input.txt', 'r')
txt = f.read()
f.close()

# txt = "16,1,2,0,4,2,7,1,2,14"

positions = list(map(int, txt.split(',')))

min_position, max_position = min(positions), max(positions)

def part1():
    fuel_used_dict = {}

    for i in range(min_position, max_position + 1):
        
        fuel_used = 0

        for p in positions:
            fuel_used += abs(p-i)
        
        fuel_used_dict.update({i: fuel_used})

    optimal_position = min(fuel_used_dict, key=fuel_used_dict.get)

    return fuel_used_dict[optimal_position]

def part2():
    fuel_used_dict = {}

    for i in range(min_position, max_position + 1):
        
        total_fuel_used = 0

        for p in positions:
            distance = abs(p-i)
            fuel_used = (distance*(distance+1))/2
            total_fuel_used += fuel_used
        
        fuel_used_dict.update({i: total_fuel_used})

    print(fuel_used_dict)

    optimal_position = min(fuel_used_dict, key=fuel_used_dict.get)

    return fuel_used_dict[optimal_position]

print(part2())