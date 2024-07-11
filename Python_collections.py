################### collections #######################

'''유용한 자료구조를 제공하는 표준 라이브러리'''
''' 대표적으로 deque와 Counter가 있다'''


#popleft() : 맨 앞에 원소 제거
#pop() : 마지막 원소 제거
#appendleft() : 맨앞에 원소 추가
#append() : 마지막에 원소 추가

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)



## counter ##
#해당 객체 내부의 원소가 몇번씩 등장했는지를 알려준다. (원소별 등장 횟수를 세는 기능)
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))
