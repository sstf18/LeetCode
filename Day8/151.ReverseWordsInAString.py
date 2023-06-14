
class Solution: 
    def ReversWords(self, s: str) -> str: 
        words = s.split()
        left = 0 
        right = len(s) -1 
        while left < right: 
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)

#Thinking: 
# first, split each words in to words list 
# after swap each words, then using .join() method add them together 