class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lengthOfStr1, lengthOfStr2 = len(str1), len(str2)

        #helper function
        def valid(potentialSubstring): 

            #if there's a remainder, string is not divisible by substring.
            if lengthOfStr1 % potentialSubstring or lengthOfStr2 % potentialSubstring:
                return False
            
            #check how many times the string is divisble by the potential substring, and store it in a variable. 
            n1, n2 = lengthOfStr1 // potentialSubstring, lengthOfStr2 // potentialSubstring

            #using string slicing to get the characters up to the number of characters from the potentialSubString variable to store in to base. 
            base = str1[:potentialSubstring]

            #create new str1 and str2 to check if it's correct. 
            return str1 == n1 * base and str2 == n2 * base

        #brute force method that loops through each potential substring of the smallest string (str2), removing a char at the end of the string each time creating all potential substrings. 
        for i in range(min(lengthOfStr1, lengthOfStr2), 0, -1):
            #if the substring is divisible and the GCDString, return it. 
            if valid(i):
                return str1[:i]
        #else, return null
        return ""