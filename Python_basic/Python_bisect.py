################## bisect ####################

'''이진 탐색을 쉽게 구현할 수 있도록 라이브러리 제공'''
'''정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적'''

#bisect_left(배열,넣을 값): 정렬 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 찾음
#bisect_right(배열,넣을 값): 정렬 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 찾음

from bisect import bisect_left,bisect_right

a = [1,2,4,4,4,6]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))


# count_by_range() : 정렬된 리스트에서 사이에 원소값의 개수를 알 수 있다
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

list = [1,2,3,3,3,3,4,4,5,6]

print(count_by_range(list,4,4))
print(count_by_range(list,-1,3))
