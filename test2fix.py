from collections import defaultdict
class RewardPoints:
    def  __init__(self):
        self.customers = defaultdict(int)
        self.counter = 0

    def earn_points(self, customer_name, points):
        if points > 0:
            if self.counter == 0:
                self.customers[customer_name] += 500
                self.counter += 1
            self.customers[customer_name] += points

    def spend_points(self, customer_name, points):
        if customer_name in self.customers.keys():
            if points > 0 and points <= self.customers[customer_name]:
                self.customers[customer_name] -= points
                return self.customers[customer_name]
        else:
            return 0

rewardPoints = RewardPoints()
rewardPoints.earn_points("John", 520)
rewardPoints.earn_points("John", 500)
print(rewardPoints.spend_points("John", 200))
