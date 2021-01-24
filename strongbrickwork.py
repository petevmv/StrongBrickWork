import numpy as np

exit_loop = True
while exit_loop:
    try:
        N , M = map(int,(input("Enter dimenson N and number M as even integer no greatar than 100 :").split()))
    except :
        continue
    if (N % 2) == 0 and (M % 2) == 0 and N > 0 and N <= 100 and M > 0 and M <= 100:
        exit_loop = False
N_list = []
M_list = []
for i in range(N):
    N_list.append(input("Enter bricks possition separeted by space: ").split())

arr = np.array(N_list, dtype=int)
print("Layer 1 \n",arr)
arr_2 = np.zeros((N, M),dtype=int)


for i in range(0, N):
    for j in range(0, M):
        if arr_2[i,j] != 0:
            continue
        if j == len(arr_2[i]) - 1:
            arr_2[i,j] = arr[i+1,0]
            arr_2[i+1,j] = arr[i+1,0]
            break
        if arr[i,j] == arr[i,j+1]:
            arr_2[i,j] = arr[i,j]
            arr_2[i+1,j] = arr[i,j]
        else:
            brick = arr[i,j]
            if brick in arr_2:
                brick = arr[i,j+1]
            arr_2[i,j] = brick
            arr_2[i,j+1] = brick

print("Layer 2 \n", arr_2)
