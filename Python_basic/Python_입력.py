############### 입력 ##################


#대표 입출력 코드 input()
a = list(map(int, input().split()))
print(a)
''' input()으로 입력받고
    split()을 이용해서 공백 나누고
    map이용해서 int형태로 형변환 해주고
    list로 결과 반환'''
a.sort(reverse=True)
print(a)


# 변수 여러개에 나눠 입력 => 선언한 변수 개수만큼 입력 받겠다는 소리
a,b,c = map(int,input().split())
print(a,b,c)


# readline()  => input함수 보다 빠른 입력 속도를 위해 사용
import sys
data = sys.stdin.readline().rstrip()
print(data)








