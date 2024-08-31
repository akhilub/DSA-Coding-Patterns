#Approach: HashTable+Counting


# This is problem is similar to the Two Sum problem, but with a slight modular twist.
# So, here we need to find a and b such that (a + b) % 60 == 0. This can be also written as,
# => (a % 60) + (b % 60) == 60
# => (a % 60) == 60 - (b % 60)

# So if both reminder ads up to 60 we can tell it is indeed a valid pair of songs. One, edge case which we have to keep in mind is, what if (a % 60) = 0 and (b % 60) = 0 our result will be 0 + 0 = 0, this fails our intution. So to handle this case we can rewrite the equation as
# => (a % 60) == (60 - (b % 60)) % 60


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        # array which keep count of no of occurences of reminders
        count = [0]*60

        for t in time:
            rem = t % 60

            target = (60-rem) % 60

            ans+=count[target]

            count[rem]+=1

        return ans













#Competative Programming

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    ans = 0
    count = [0]*60
    for t in time:
        t%=60
        ans+=count[(60-t)%60]
        count[t]+=1
    return ans

