n= int(input())
number_list= list(map(int,input().split()))
result = 0

for i in number_list:
    cnt = 0
    if i == 1:
        continue
        
    for j in range(2,i+1):
        if i % j == 0:
            cnt +=1
    if cnt == 1:
        result += 1

print(result)






