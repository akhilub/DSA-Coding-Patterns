class Solution:
    def dayOfYear(self,date:str)->int:
        year,month,day = (int(s) for s in date.split("-")) #Notice the spiliting of the string
        f = 29 if year % 400 == 0 or (year % 100!=0 and year % 4 ==0) else 28
        days = [31,f,31,30,31,30,31,31,30,31,30,31]

        return sum(days[:month -1]) + day

#Just Another way of writing the code
class Solution:
    def dayOfYear(self,date:str)->int:
        y , m , d = list(map(int, date.split('-'))) #Notice the spiliting of the string
        f = 29 if y %400 == 0 or (y%100!=0 and y%4==0) else 28
        days = [31,f,31,30,31,30,31,31,30,31,30,31]

        return sum(days[:month - 1]) + d  

