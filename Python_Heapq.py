################### Heapq ########################


# 다익스트라 최단 경로 알고리즘 등 우선순위 큐 기능을 구현하고자 할 때 사용.
'''
    힙 구조: 이진트리 형태의 자료구조
    최소 힙: 부모노드의 값이 자식 노드보다 작거나 같다
    최대 힙: 부모노드의 값이 자식 노드보다 크거나 같다
'''

# 힙에 원소를 삽입 => heapq.heappush()
# 힙에 원소를 꺼낼때 => heapq.heappop()

import heapq


# 힙정렬 예제 (오름차순)
def heapsort(iterable):
    h=[]
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)



# 힙정렬 예제 (내림차순) / 파이썬은 최대힙을 지원안함 그래서 -로 역으로 넣었다가 꺼낼때 다시 돌림
def heapsort2(iterable):
    h=[]
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1,3,5,7,9,2,4,6,8,0])
print(result)