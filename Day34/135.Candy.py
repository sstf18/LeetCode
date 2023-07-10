from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # since every kids has last one candy
        candy = [1]*len(ratings)
    
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1 

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # max() is important left anf right diff
                # so we should choose the max.val()
                candy[i] = max(candy[i + 1] + 1, candy[i])
        result = sum(candy)
        return result

