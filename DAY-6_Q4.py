# Program to check if Nums form a friendly pair?
class Solution:
    def getSumOfDivisors(self, num):
        total = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i and i != 1:
                    total += num // i
        return total + (0 if num == 1 else num)  # include the number itself

    def isFriendlyPair(self, a, b):
        sum1 = self.getSumOfDivisors(a)
        sum2 = self.getSumOfDivisors(b)
        
        return sum1 * b == sum2 * a  # Cross multiply to avoid float errors
