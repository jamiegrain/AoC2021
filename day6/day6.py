from functools import lru_cache

# Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

lanternfish_timers: list = list(map(int, txt.split(',')))

class LanternFish:

    def __init__(self, time_left = 8):
        self.time_left = time_left

    def decrement(self):
        if self.time_left:
            self.time_left = self.time_left - 1
        else:
            self.time_left = 6

laternfish: list = [LanternFish(t) for t in lanternfish_timers]

def part1():

    for i in range(21):
        n_reproducing: int = 0
        for fish in laternfish:
            if fish.time_left == 0:
                n_reproducing += 1

        for fish in laternfish:
            fish.decrement()

        for new_fish in range(n_reproducing):
            laternfish.append(LanternFish())

    return len(laternfish)

# This is the answer for part 1
# print(part1())

# The approach for part 1 is too slow for part 2

# Let's make a hash map
# This maps the number of fish with
fish_dict: dict = dict(zip(list(range(9)), [0] * 9))

for fish in laternfish:
    fish_dict.update({fish.time_left: fish_dict.get(fish.time_left, 0) + 1})

for i in range(256):

    n_reproducing: int = fish_dict[0]

    for j in range(8):
        fish_dict[j] = fish_dict[j+1]

    fish_dict[6] += n_reproducing

    fish_dict[8] = n_reproducing

n_fish: int = 0

for k, v in fish_dict.items():
    n_fish += v

print(n_fish)