############### itertools ################
''' 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리'''

#대표 클래스 2가지
#permutations: 이터러블 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산해준다 /리스트 자료형으로 변환해서 사용
#combinations: 이터러블 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우의 수 / ''
#product: permutations와 같지만 중복을 허용하여 모든 경우의 수를 뽑는다. / 즉 자기 자신 포함
#combinations_with_replacement: combinations와 같지만 중복을 허용한다. / 즉 자기 자신 포함


from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

#permutations 클래스 사용 나열 경우의수
data = ['a','b','c']
result = list(permutations(data,3))
print(result)
print(len(result))


#combinations 클래스 사용 순서 고려x 나열
result2 = list(combinations(data,2))
print(result2)
print(len(result2))


#product 클래스 사용
result3 = list(product(data,repeat=2))
print(result3)
print(len(result3))


#combinations_with_replacement 클래스 사용
result4 = list(combinations_with_replacement(data,2))
print(result4)
print(len(result4))