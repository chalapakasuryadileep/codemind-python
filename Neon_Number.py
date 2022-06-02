n=int(input())
sq=n**2
sum=0
while sq>0:
    r=sq%10
    sum=sum+r
    sq=sq//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')