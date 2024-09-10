class Solution:
    def firstBadVersion(self, n: int) -> int:
        L , R = 1 , n
        while L<=R:                 #while L<R:
            mid = (L+R)//2
            if isBadVersion(mid):
                R = mid - 1         #R = mid
            else:
                L = mid + 1
        return L