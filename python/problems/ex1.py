class Solution(object):
    def __gcd(self,c,d):
        if(d == 0):
            return c
        return self.__gcd(d,c%d)
    def nthMagicalNumber(self,n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        if(a>b):
            return nthMagicalNumber(self,n,a,b)
        m = int(1e9 + 7)
        l = a / self.__gcd(a, b) * b
        if(b%a == 0):
            return int((l* a * n)% m)
        a = a / self.__gcd(a, b) * b
        lo = a
        hi = lo * n
        while (lo < hi):
            mi = lo + (hi - lo) / 2
            c = mi / a + mi / b - mi / l
            if(c < n):
                lo = mi + 1
            else:
                hi = mi
        return int(lo % m)

s = Solution()
print(s.nthMagicalNumber(4, 2, 3))
