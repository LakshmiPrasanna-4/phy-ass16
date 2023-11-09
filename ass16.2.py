# Write a program to print the prime count of the given number.

n=int(input())
c=0
for i in range(1,n):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        c=c+1

print(c)

    
