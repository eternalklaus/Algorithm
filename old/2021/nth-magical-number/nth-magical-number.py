class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # Not linear, but conclude brillient idea
        
        # lcm and gcd
        
        def getgcd(a, b):
            a, b = min(a,b), max(a,b) 
            while a:
                tmp = a
                a = b % a
                b = tmp
            return b
        
        lcm = a*b//getgcd(a,b)
        a_list = [i * a for i in range(1, lcm//a)]
        b_list = [i * b for i in range(1, lcm//b)]
        ab_list = sorted(a_list + b_list + [0])
        
        quotient = n // len(ab_list)
        remainder = n % len(ab_list)
        
        output = 0
        output += lcm * quotient
        output += ab_list[remainder]
        return output % (10**9 + 7)
        
        
        
        