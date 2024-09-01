#Approach: Prefix Product
# Time: Constructor: O(1), add(num: int): O(1), getProduct(k: int): O(1)
# Space: O(∣add(num: int)∣)

'''
We initialize an array `s` where `s[i]` represents the product of the first `i` numbers.

When calling `add(num)`, we judge whether `num` is `0`. 
If it is, we set `s` to `[1]`. Otherwise, we multiply the last element of `s` by `num` and add the result to the end of `s`.

When calling `getProduct(k)`, we now judge whether the length of `s` is less than or equal to `k`. 
If it is, we return `0`. Otherwise, we return the last element of `s` divided by the `k+1`th element from the end of `s`. 
That is, `s[-1]/s[-k-1]`.

The time complexity is O(1), and the space complexity is O(n). Where n is the number of times `add` is called.
'''

class ProductOfNumbers:

    def __init__(self):
        self.s = [-1]
        

    def add(self, num: int) -> None:
        if num ==0:
            self.s=[1]
            return
        self.s.append(self.s[-1]*num)

    def getProduct(self, k: int) -> int:
        return 0 if len(self.s)<=k else self.s[-1]//self.s[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

