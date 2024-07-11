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


#리스트의 인덱싱
b = [1,2,3,4,5,6,7,8,9]
print(b[-1])
print(b[-3])

b[1] = 10
print(b)


#리스트의 슬라이싱 (끝 인덱스의 경우 1을 뺀 값의 인덱스 까지 처리)
print(b[3:5])   
print(b[0:2])


#리스트 컴프리헨션 (리스트를 초기화 하는 방법)
array = [i for i in range(20) if i %2 ==1]
print(array)

array = [i*i for i in range(1,10)]
print(array)

# N*M 크기의 2차원 리스트를 초기화 하기
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)





##### 리스트 관련 메서드####
# append(): 원소 삽입
list = [i for i in range(1,11)]
list.append(11)
print(list)

#sort(): 정렬기능(오름차순, 내림차순)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#reverse(): 원소를 모두 뒤집어 놓는다.
list.reverse()
print(list)

#insert(): 특정한 인덱스 위치에 원소 삽입
list.insert(0,0)
print(list)

#count(): 특정값의 데이터 개수를 센다.
cnt = list.count(0)
print(cnt)

#remove(): 특정 원소를 하나 제거한다.
list.remove(0)
print(list)


########## 리스트 자료형 활용 ############
remove_set = {3,5}
#기존 리스트에서 특정 값들을 제거하고 뽑아야 할때 사용
resultList = [i for i in list if i not in remove_set] 
print(resultList)

