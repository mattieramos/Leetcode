class Solution(object):
    def mySqrt(self, x):
        start = 1
        end = x // 2

        if x < 2:
            return x
        while start <= end:
            middle = ((start + end) // 2)
            middle_sqr = middle * middle

            if middle_sqr < x:
                start = middle + 1
            elif middle_sqr > x:
                end = middle - 1
            else:
                return middle

        if middle_sqr > x:
            return middle - 1
        else:
            return middle