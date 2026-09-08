class DailyMessage:
    def __init__(self): self.msg = ""
    def get(self): self.msg = input("Enter today's message: ")
    def show(self): print(self.msg.upper())

class HelperSession:
    def __init__(self): print("Session started")
    def __del__(self): print("Session ended")

class PairFinder:
    def find(self, nums, target):
        lookup = {}
        for i, n in enumerate(nums):
            if target - n in lookup: return lookup[target - n], i
            lookup[n] = i

DailyMessage().get(); DailyMessage().show()
session = HelperSession()
nums = (10,20,30,40,50,60,70)
res = PairFinder().find(nums, int(input("Enter target sum: ")))
print(res if res else "No match")
del session
