month,day,year,time = input().split()
day,year,time = int(day[:-1]),int(year),int(time[:2])*60+int(time[3:])
M = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

if (year%4 == 0 and year%100 != 0) or (year%400 == 0): # 윤년이면
    Y = [(0,0),(1,31),(2,29),(3,31),(4,30),(5,31),(6,30),(7,31),(8,31),(9,30),(10,31),(11,30),(12,31)]
else:
    Y = [(0,0),(1,31),(2,28),(3,31),(4,30),(5,31),(6,30),(7,31),(8,31),(9,30),(10,31),(11,30),(12,31)]

tot = 0
for i in range(1,13):
    tot += Y[i][1]
tot*= (24*60)

now = 0
for i in range(1,M[month]):
    now += Y[i][1]
now*= (24*60)
now += (day-1)*24*60 + time

print((now/tot)*100)