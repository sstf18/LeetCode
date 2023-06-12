class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True: 
            n = self.get_sums(n)
            if n == 1: 
                return True
            if n in record: 
                return False
            else: 
                record.add(n)
    def get_sums(self, n: int) -> int: 
        new_sum = 0
        while n: 
            # divmod method: quotient and remainder, division and modulo
            n , r = divmod(n, 10)
            new_sum += r ** 2
        return new_sum

# Thinking:
# using set() method, to determind wheather n is in record. 
# in get_sums, be care for using get_sums