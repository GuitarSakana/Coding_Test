#리스트 자료형#

#대괄호 안에  원소를 넣어 초기화
#쉼표로 원소 구분
#원소에 접근할때는 인덱스로 접근
#인덱스는 0번부터 시작

a = []
b = list()

print(a)
print(b)

a.append(1)
print(a)
print(a[0])

c = [1,2,3,4,5]
print(c)
print(c[1])


#주어진 크기(n)만큼 리스트 초기화
n =10
a = [0]*n
print(a)