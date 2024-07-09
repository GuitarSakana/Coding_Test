########### Set 자료형 ###########

# Set자료형 특징
''' 
    중복을 허용하지 않음
    순서가 없음
'''

#set 생성 - 중괄호를 사용해서 만든다/ set()으로 생성
data = set([1,2,3,4,5])
print(data)
data1 = {6,7,8,9}
print(data1)


#집합 자료형의 연산 (합집합, 차집합, 교집합)
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a|b)  #중복은 제외하고 합침
print(a&b)  #공통된 데이터만 출력
print(a-b)  #공통된 데이터 빼고 남은 데이터만 출력


#######관련 함수#######
set_list = {1,2,3,4,5,6,7}
#add(): 값을 추가
set_list.add(10)
print(set_list)

#update(): 여러개의 값을 추가
set_list.update([11,12])
print(set_list)

#remove(): 특정한 값을 제거
set_list.remove(12)
print(set_list)