class Solution(object):
    def mySqrt(self, x):

        # You can brute force check every number that leads up to x, but that could take forever and since you have to check every number individually, it would be an O(1) time complexity.

        # will use Binary Search to quickly check middle element. 

        # PSEUDO:

        # create start and end pointers
        # end pointer will have to be x // 2, since x/2 is the highest a square root would be the highest a perfect squareroot would be. 

        # since 0 and 1 don't have square roots, if x is < 2, return x. 

        # BASE CASE:
        # while start <= end:
        #     middle
        #     will also create a middle_sqrd to check values

        # if middle_sqrd < x
        #     start = middle + 1
        # elif middle_sqrd > x
        #     end = middle - 1
        # else
        #     return middle
        # For non-perfect squares, the computed middle value might exceed the actual square root, requiring us to round down. To handle this, we check if middle * middle > x. If this condition is met, we return middle - 1 to ensure we correctly round down to the nearest integer.


        start = 1
        end = x // 2

        if x < 2:
            return x

        while start <= end:
            middle = (start + end) // 2
            middle_sqrd = middle * middle

            if middle_sqrd > x:
                end = middle - 1
            elif middle_sqrd < x:
                start = middle + 1
            else:
                return middle

        if middle_sqrd > x:
            return middle - 1
        else:
            return middle
            