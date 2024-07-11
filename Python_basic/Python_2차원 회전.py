'''2차원 리스트를 90도로 회전시키는 함수'''

def rotate_a_matrix_by_90_degree(list):
    row_length = len(list)
    column_length = len(list[0])

    res = [[0]*row_length for _ in range(column_length)]
    
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length -1 -r] = list[r][c]
    
    return res

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(f"{a[i][j]:<2}",end=" ")
    print()

print()
res = rotate_a_matrix_by_90_degree(a)

for i in range(len(res)):
    for j in range(len(res[i])):
        print(f"{res[i][j]:<2}",end=" ")
    print()
