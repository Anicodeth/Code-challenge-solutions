
class Solution:
    def __init__(self, nums: List[int]):
        self.index_dict = defaultdict(list)
        for i in range(len(nums)):
            self.index_dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_dict[target])
