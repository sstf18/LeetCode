from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #using map
        five = 0
        ten = 0 
        twenty = 0

        for i in bills:
            if i == 5: 
                five += 1 

            if i == 10: 
                if five <= 0: 
                    return False
                ten += 1
                five -= 1

            if i == 20: 
                if five > 0 and ten > 0: 
                    five -= 1
                    ten -= 1
                elif five >= 3: 
                    five -= 3
                else: 
                    return False

        return True


            