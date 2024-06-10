#MyApproach: Greedy
# DS : HashTable

#Notice I have created the valSym List of Tuple (val,sym) in desecending order the way we do division intutively
# While creating do write two tuple at a time

#TC : O(m) 
#SC :O(m)
class Solution:
    def intToRoman(self,num):
        valSym = [(1000,'M'),(900,'CM'),
                (500,'D'),(400,'CD'),
                (100,'C'),(90,'XC'),
                (50,'L'),(40,'XL')
                (10,'X'),(5,'V'),
                (1,'I')]
        res = ''
        for val,sym in valSym:
            if num // val:
                count = num // val
                res+=(sym*count)
                num = num % val
        return res 



#Approach :Greedy

#We can first list all possible symbols cs and their corresponding values vs, then enumerate each value vs[i] from large to small. 
#Each time, we use as many symbols cs[i] corresponding to this value as possible, until the number num becomes 0.


#Just another way of writing Greedy
#Notice the use of zip() to make tuple for iteration



class Solution:
    def intToRoman(self,num):
        cs = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'V', 'IV' ,'I')
        vs = (1000, 900,  500,  400, 100,  90,   50,  40,   10,  5,    4,   1)
        ans = []
        for c , v in zip(cs,vs):
            while num>=v:
                num-=v
                ans.append(c)
        return ''.join(ans)




