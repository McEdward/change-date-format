import itertools
class MovingTotal:
    def __init__(self):
        self.t = []
        self.total = []
        self.numbers = []
    def append(self, x):
        for i in x:
            self.numbers.append(i)

    def contains(self, total):
        totals = itertools.combinations(self.numbers, 3)
        for i in totals:
            x = sum(i)
            self.t.append(x)
        return total in self.t


movingtotal = MovingTotal()
movingtotal.append([1,2,3])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([4])
print(movingtotal.contains(9))
