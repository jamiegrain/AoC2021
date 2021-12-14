f = open('input.txt', 'r')
txt = f.read()
f.close()

lines = txt.splitlines()

letters = list(lines[0])

mapping = lines[2:]

mapping_dict = {}

for l in mapping:
    mapping_dict.update({l.split(' -> ')[0]: l.split(' -> ')[1]})

letter_pair_count = {}

def convert_initial_list():
    for i in range(len(letters) - 1):
        letter_pair = letters[i] + letters[i + 1]
        letter_pair_count.update({letter_pair: letter_pair_count.get(letter_pair, 0) + 1})

convert_initial_list()

def iterate(letter_pair_count):
    new_letter_pair_count = {}
    for pair, n in letter_pair_count.items():
        new_letter = mapping_dict.get(pair)
        first_new_pair = pair[0] + new_letter
        second_new_pair = new_letter + pair[1]
        new_letter_pair_count.update({first_new_pair: new_letter_pair_count.get(first_new_pair, 0) + n})
        new_letter_pair_count.update({second_new_pair: new_letter_pair_count.get(second_new_pair, 0) + n})
    return new_letter_pair_count

for i in range(40):
    letter_pair_count = iterate(letter_pair_count)
    print(i)

print(letter_pair_count)

def part1(letter_pair_count):
    letter_dict = {}
    for pair, n in letter_pair_count.items():
        letter_dict.update({pair[0]: letter_dict.get(pair[0], 0) + n})
    
    letter_dict.update({letters[-1]: letter_dict.get(letters[-1], 0) + 1})

    most_common = max(letter_dict, key=letter_dict.get)
    least_common = min(letter_dict, key=letter_dict.get)

    print(letter_dict)

    return letter_dict[most_common] - letter_dict[least_common]

print(part1(letter_pair_count))