import itertools
class MovingTotal:
    def __init__(self):
        self.t = []
        self.numbers = []
    def append(self, x):
        for i in x:
            self.numbers.append(i)

    def contains(self, total):
        self.totals = set(itertools.combinations(self.numbers, 3))
        for i in self.totals:
            x = sum(i)
            self.t.append(x)
        b = total in self.t
        self.t = []
        return b


movingtotal = MovingTotal()
movingtotal.append([1,2,3])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([4])
print(movingtotal.contains(9))

print(movingtotal.contains(12))
movingtotal.append([5,6])
print(movingtotal.contains(12))
