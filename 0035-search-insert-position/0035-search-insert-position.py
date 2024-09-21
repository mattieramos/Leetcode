class Solution(object):
    def searchInsert(self, nums, target):
       #create array of nums
       #high = list[nums] - 1
       #low = nums[0]
       #mid = (high + low) // 2

       #(base case) while low <= hight
       #if target > mid
            #low = mid + 1
        
        #elif target < mid
            # high == mid - 1
        #else
            #mid = target

        #return mid
        

        #*** creating variables ****
        low = 0
        high = len(nums) - 1
        
        #base case
        while low <= high:
            middle = (low + high) // 2

            #if guess (middle) is to low, go higher
            if nums[middle] < target:
                low = middle + 1
            
            #if guess is too high, go lower
            elif nums[middle] > target:
                high = middle - 1
            
            # if guess if not higher or lower than target, return it
            else:
                return middle

        return low
