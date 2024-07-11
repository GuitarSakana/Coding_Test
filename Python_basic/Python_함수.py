############## 함수 ###############

#기본 함수 형태
def add(a,b):
    return a+b
print(add(4,5))


# global키워드 => 전역변수를 함수 내부에서 접근
a=10
def testGlobal():
    global a
    a=1
print(a)
testGlobal()
print(a)


# 람다 함수
print((lambda a,b: a+b)(3,5))