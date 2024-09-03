#Approach:Simulation
'''
We start traversing from the last element of the array, add one to the current element, and then take the modulus by 10. 
If the result is not 0, it means that there is no carry for the current element, and we can directly return the array. 

Otherwise, the current element is 0 and needs to be carried over. We continue to traverse the previous element and repeat the above operation. 
If we still haven't returned after traversing the array, it means that all elements in the array are 0, and we need to insert a 1 at the beginning of the array.

The time complexity is O(n), where n is the length of the array. Ignoring the space consumption of the answer, the space complexity is O(1).
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits



#My Approach
#TC:O(n)
#SC:O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def makeNumber(digits:List[int])->int:
            num=0
            for dig in digits:
                num = num*10+dig
            return num
        
        def getDigits(num:int)->List[int]:
            lst = []
            while num>0:
                r = num%10
                lst.append(r)
                num=num//10
            return lst[::-1]
        
        plusOneNum = makeNumber(digits)+1
        
        return getDigits(plusOneNum)
    
    
    
#Python One Liners
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
                
        makeNumber = lambda digits: reduce(lambda num, dig: num * 10 + dig, digits, 0)
        
        
        getDigits = lambda num:list(map(int,str(num)))
        
        
        plusOneNum = makeNumber(digits)+1
        
        return getDigits(plusOneNum)


#Learn Conversion(str to int and int to str) from here
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(d) for d in digits]))
        plusOne = num+1
        return [int(d) for d in str(plusOne)]
        
        