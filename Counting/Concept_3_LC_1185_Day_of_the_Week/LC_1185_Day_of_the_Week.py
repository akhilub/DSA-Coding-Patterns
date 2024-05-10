class Solution:
    def dayofTheWeek(self,day,month,year):
        f = 29 if year % 400 or (year % 4 ==0 and year % 100 != 0) else 28 
        days = [31,f,31,30,31,30,31,31,30,31,30,31]

        week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        cdays = 0
        for i in range(1971,year):
            cday+= 366 if i % 4 == 0 else 365

        for i in range(month-1):
            cdays+=days[i]

        cdays+=day

        return week[(cdays+4)%7]