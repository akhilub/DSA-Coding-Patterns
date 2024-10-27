class Solution:
    #Using Addition Swap
    def swapWithoutAllocatingMemory(self,a,b):
        a = a+b         #a^b
        b = a-b         #a^b
        a = a-b         #a^b
        return a,b
    
    
    #Using XOR Swap
    def swapWithoutAllocatingMemory2(self,a,b):
        a = a^b
        b = a^b
        a = a^b
        return a,b
        
    
    
if __name__=="__main__":
    a = 1
    b = 15
    print(Solution().swapWithoutAllocatingMemory(a,b))
    print(Solution().swapWithoutAllocatingMemory2(a,b))
    