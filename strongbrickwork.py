import numpy as np

exit_loop = True
while exit_loop:
    try:
        N , M = map(int,(input("Enter dimenson N and number M as even integer no greatar than 100 :").split()))
    except :
        print("==Please Enter valid dimension==")
        continue
    if (N % 2) == 0 and (M % 2) == 0 and N > 0 and N <= 100 and M > 0 and M <= 100:
        exit_loop = False

N_list = []
for i in range(N):
    N_list.append(input("Enter numbers to form bricks separeted by space: ").split())
    print(N_list[i])

    if len(N_list[i]) != M:
        print("You have entered more elements than required based on you'r {}x{} input, entering first {} of them".format(N, M, M))
        N_list[i] = N_list[i][0:M]
        print(N_list)
arr = np.array(N_list, dtype=int)
print("Layer 1 (input) \n",arr)
arr_2 = np.zeros((N, M),dtype=int)

try:
    for i in range(0, N):
        for j in range(0, M):
            if arr_2[i,j] != 0:
                continue
            if j == len(arr_2[i]) - 1:

                arr_2[i,j] = arr[i+1,0]
                arr_2[i+1,j] = arr[i+1,0]
                print(len(arr_2[i])-1, j)
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
except:
    print("-1 \n No solution found")
print("Layer 2 (output) \n", arr_2)
