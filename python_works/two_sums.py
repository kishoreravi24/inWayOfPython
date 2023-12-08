# This code have some flaws in logic but !
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper_list:List[int] = []
        for item in nums:
            res = target-item
            if res in helper_list:
                return [nums.index(res),nums.index(item)]
            else:
                helper_list.append(item)
