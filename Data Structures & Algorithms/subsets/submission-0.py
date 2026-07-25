class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:

            current_size = len(res)

            for i in range(current_size):

                new_subset = res[i].copy()

                new_subset.append(num)

                res.append(new_subset)

        return res
        