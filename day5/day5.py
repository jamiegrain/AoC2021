import re

# Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

inpt: list = txt.splitlines()

lines = []

class Line:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.direction = self.get_direction()
        self.points_affected = self.find_points_affected()

    def get_direction(self):
        """
        Get direction of line
        d = diagonal
        v = vertical
        h = horizontal
        """
        if self.start[0] != self.end[0] and self.start[1] != self.end[1]:
            return 'd'
        elif self.start[0] == self.end[0]:
            return 'v'
        elif self.start[1] == self.end[1]:
            return 'h'
        else:
            raise Exception("Couldn't work out direction of line")


    def find_points_affected(self):
        points_affected = []
        if self.direction == 'd':
            # Top left
            if self.start[1] <  self.end[1] and self.start[0] < self.end[0]:
                for i in range(self.end[1] - self.start[1] + 1):
                    # breakpoint()
                    points_affected.append((self.start[0] + i, self.start[1] + i))
            # Bottom left
            elif self.start[1] > self.end[1] and self.start[0] < self.end[0]:
                for i in range(self.end[0] - self.start[0] + 1):
                    # breakpoint()
                    points_affected.append((self.start[0] + i, self.start[1] - i))
            # Top right
            elif self.start[1] < self.end[1] and self.start[0] > self.end[0]:
                for i in range(self.start[0] - self.end[0] + 1):
                    # breakpoint()
                    points_affected.append((self.start[0] - i, self.start[1] + i))
            # Bottom right
            elif self.start[1] > self.end[1] and self.start[0] > self.end[0]:
                for i in range(self.start[1] - self.end[1] + 1):
                    points_affected.append((self.start[0] - i, self.start[1] - i))
            return points_affected
        elif self.direction == 'v':
            for i in range(min(self.start[1], self.end[1]), max(self.start[1], self.end[1]) + 1):
                points_affected.append((self.start[0], i))
            return points_affected
        elif self.direction == 'h':
            for i in range(min(self.start[0], self.end[0]), max(self.start[0], self.end[0]) + 1):
                points_affected.append((i, self.start[1]))
            return points_affected
        else:
            return []


for l in inpt:
    nums = re.findall('\d*[^,\s\->]', l)
    start, end = list(map(int, nums[:2])), list(map(int, nums[2:]))
    line = Line(start, end)
    lines.append(line)

points_affected_dict = {}
for l in lines:
    for p in l.points_affected:
        points_affected_dict.update({p: points_affected_dict.get(p, 0) + 1})

n_double_points = 0
for p, c in points_affected_dict.items():
    if c > 1:
        n_double_points += 1

print(n_double_points)