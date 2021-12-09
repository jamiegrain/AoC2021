#Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

#Convert input to list
measurements: list = txt.split()

measurements = [int(m) for m in measurements]

n_increases: int = 0

for i in range(1, len(measurements)):
    if measurements[i] > measurements[i - 1]:
        n_increases += 1
    
# Task 1 answer
print(n_increases)

# Task 2

n_increases = 0

for i in range(2, len(measurements)):
    val1: int = measurements[i-1] + measurements[i-2] + measurements[i-3]
    val2: int = measurements[i] + measurements[i-1] + measurements[i-2]
    if val2 > val1:
        n_increases += 1

print(n_increases)