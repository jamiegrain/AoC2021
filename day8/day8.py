# Extract the input

f = open('input.txt', 'r')
txt: str = f.read()
f.close()

displays: list = txt.splitlines()


sample_values: list = [d.split('|')[0] for d in displays]
sample_values = [v.split() for v in sample_values]

output_values: list = [d.split('|')[1] for d in displays]
output_values = [v.split() for v in output_values]

decodes_list = []

for s in sample_values:
    num_decode_dict = dict(zip(range(10), [''] * 10))
    digit_decode_dict = {}

    for digit in s:
        if len(digit) == 2:
            num_decode_dict.update({1: digit})
            digit_decode_dict.update({digit: 1})
        elif len(digit) == 7:
            num_decode_dict.update({8: digit})
            digit_decode_dict.update({digit: 8})
        elif len(digit) == 3:
            num_decode_dict.update({7: digit})
            digit_decode_dict.update({digit: 7})
        elif len(digit) == 4:
            num_decode_dict.update({4: digit})
            digit_decode_dict.update({digit: 4})

    for digit in s:
        if len(digit) == 5 and len(set(digit).intersection(num_decode_dict[1])) == 2 and len(set(digit).intersection(num_decode_dict[1])) == 2:
            num_decode_dict.update({3: digit})
            digit_decode_dict.update({digit: 3})
        if len(digit) == 6 and len(set(digit).intersection(num_decode_dict[1])) == 1 and len(set(digit).intersection(num_decode_dict[1])) == 1:
            num_decode_dict.update({6: digit})
            digit_decode_dict.update({digit: 6})
        if len(digit) == 6 and len(set(digit).intersection(num_decode_dict[4])) == 4:
            num_decode_dict.update({9: digit})
            digit_decode_dict.update({digit: 9})
        if len(digit) == 6 and len(set(digit).intersection(num_decode_dict[4])) == 3 and len(set(digit).intersection(num_decode_dict[1])) == 2:
            num_decode_dict.update({0: digit})
            digit_decode_dict.update({digit: 0})

    for digit in s:
        if len(digit) == 5 and len(set(digit).intersection(num_decode_dict[6])) == 5:
            num_decode_dict.update({5: digit})
            digit_decode_dict.update({digit: 5})
        if len(digit) == 5 and len(set(digit).intersection(num_decode_dict[6])) == 4 and len(set(digit).intersection(num_decode_dict[1])) == 1:
            num_decode_dict.update({2: digit})
            digit_decode_dict.update({digit: 2})
        
        
    decodes_list.append(digit_decode_dict)


def part1():

    n_1478: int = 0

    for output in output_values:
        for val in output:
            if len(val) in (2,4,3,7):
                n_1478 += 1

    return n_1478

def part2():

    converted_outputs_sum: int = 0

    for i, output in enumerate(output_values):
        converted_output: str = ""
        decoder: dict = decodes_list[i]
        for val in output:
            for k in decoder.keys():
                if set(val) == set(k):
                    converted_output += str(decoder[k])
        print(converted_output)
        converted_outputs_sum += int(converted_output)

    return converted_outputs_sum
    

print(part2())