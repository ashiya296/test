# a="python"
# for i in range(0,len(a)+1):
#     for j in range(0,i+1):
#         print(a[j], end=" ")
#     print(" ")     
n=int(input("enter a number"))
count=1
# if(n>1):
#     for i in range(1,n+1):
#         if(n%i)==0:
#             count=count+1
#     if(count==2):
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime")    

for i in range(1,n+1):
    count=i*count
print(count)    