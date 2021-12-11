f = open('input.txt', 'r')
txt: str = f.read()
f.close()

lines: list = txt.splitlines()

char_dict: dict = {'(': ')', '{': '}', '[': ']', '<': '>'}

def part1():

    illegal_char_scores: dict = {')': 3, '}': 1197, ']': 57, '>': 25137}

    error_score: int = 0

    for line in lines:

        chars: list = []

        for char in line:
            if char in char_dict.keys():
                chars.append(char)
            elif chars and char == char_dict.get(chars[-1]):
                chars.pop()
            else:
                error_score += illegal_char_scores.get(char)
                break

    return error_score

def part2():

    autocomplete_scores: list = []
    autocomplete_scoring_dict: dict = {'(': 1, '{': 3, '[': 2, '<': 4}

    for line in lines:

        chars: list = []
        is_corrupted = False

        for char in line:
            if char in char_dict.keys():
                chars.append(char)
            elif chars and char == char_dict.get(chars[-1]):
                chars.pop()
            else:
                is_corrupted = True
                break

        # Once we've done the for loop check for incomplete lines
        if not is_corrupted:
            autocomplete_score: int = 0
            for char in chars[::-1]:
                autocomplete_score *= 5
                autocomplete_score += autocomplete_scoring_dict.get(char)
            autocomplete_scores.append(autocomplete_score)

    middle_score = sorted(autocomplete_scores)[len(autocomplete_scores)//2]

    return middle_score

print(part2())