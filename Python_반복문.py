################## 반복문 ###################


# While문
i =1
result =0
while i<=9:
    result+=i
    i+=1
print(result)

i=1
result = 0
while i<=9:
    if i%2==1:
        result += i
    i+=1
print(result)


# for문
list = [1,2,3,4,5,6,7]
for i in list:
    print(i,end=" ")

for e in range(10):
    print(e)

for i in range(1,10):
    print(i,end=" ")
print()

#for문을 이용한 구구단
for i in range(2, 10):
    for j in range(2, 10):
        print(f"{j} x {i} = {i*j:2}", end="   ")
    print()