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
            for j in range(0,len(self.numbers)-1):
                if i[0] == self.numbers[j] and i[1] == self.numbers[j+1] and i[2] == self.numbers[j+2]:
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
