class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # Base case: if N is 1, return an array with a single element [1]
        if n==1:
            return [1]
        
        #Recursively construct the beautiful array for odd and even parts
        
        odd = self.beautifulArray((n>>1)//1)
        even = self.beautifulArray(n>>1) 
        
        # Transform and populate the odd and even parts in the result
        # Each odd element is 2*value - 1 and each even element is 2*value
        
        left = [2*x-1 for x in odd]
        right = [2*x for x in even]
        
        return left+right
    
    
'''
odd = self.beautifulArray((n+1)//2)

            ||
        equivalent
            ||
            
odd = self.beautifulArray((n>>1)//1)






even = self.beautifulArray(n//2)

            ||
        equivalent
            ||

even = self.beautifulArray(n>>1) 


'''