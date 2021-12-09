#Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

# Get the numbers as a list of strings
nums: list = txt.split()

# Create a dict for counting
bit_count: dict = {}

for n in nums:
    for i in range(len(n)):
        if n[i] == '1':
            bit_count.update({i: bit_count.get(i, 0) + 1})

bit_ratio: dict = {}
for i in range(len(bit_count.keys())):
    bit_ratio[i] = bit_count[i] / len(nums)

gamma: str = ''
eps: str = ''
for k in range(len(bit_ratio)):
    if bit_ratio[k] > 0.5:
        gamma += '1'
        eps += '0'
    else:
        gamma += '0'
        eps += '1'

# Part 1 answer
# print(int(gamma, 2) * int(eps, 2))

# Part 2
# For each digit in the numbers
for i in range(len(nums[0])):

    # If only one number left break
    if len(nums) == 1:
        break

    # For each column, count the number of 1s and 0s
    n_1s: int = 0
    n_0s: int = 0

    for n in nums:
        if n[i] == '1':
            n_1s += 1
        else:
            n_0s += 1

    print(n_1s, n_0s)

    # If there are more 1s than 0s reduce nums
    if n_1s > n_0s:
        nums = list(filter(lambda x: True if x[i] == '0' else False, nums))
    elif n_0s > n_1s:
        nums = list(filter(lambda x: True if x[i] == '1' else False, nums))
    else:
        nums = list(filter(lambda x: True if x[i] == '0' else False, nums))

print(int(nums[0], 2))
print(2039 * 3649)