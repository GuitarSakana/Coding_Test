##############사전 자료형#############

'''키와 값을 쌍으로 가지는 자료형 (java에서의 Map과 같음)'''
'''
    내부적으로 해시 테이블을 이용
    리스트보다 훨씬 빠르게 동작
'''

data = dict()
data['사과'] = 'Apple'
data['수량'] = 4
print(data)

#사전 자료형에서 데이터 찾기
if '사과' in data:
    print("사과가 존재합니다")


#사전 자료형 관련 함수
data1 = dict()
data1['사과'] = 'Apple'
data1['바나나'] = 'Banana'
data1['코코넛'] = 'Coconut'

key_list = data1.keys()
value_list = data1.values()

print(key_list)
print(value_list)

for key in key_list:
    print(key)