############### 조건문 ##################

#if문
x= 15
if x>=15:
    print(x)

if x==1:
    print("x =1")
elif x<15:
    print("x는 15보다 작음")
else:
    print("x는 ",x)


#if문에서 pass => 아무것도 처리하지 않고 그냥 넘기고 싶을때 사용
score = 80
if score >=80:
    pass
else:
    print("과락 재시험 필")


#조건이 하나일때 if문 (파이썬에서 3항 연산자)
result = "Success" if score >=80 else "Fail"
print(result)


#리스트에서 조건문 응용
a = [1,2,3,4,5,5,5]
remove_set ={3,5}
result = [i for i in a if i not in remove_set]
print(result)