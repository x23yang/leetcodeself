#求数组a的不相邻的元素的和的最大值
a=[1,2,4,1,7,8,3]
def rec_arr(arr,i):
    if i == 0 :
        return arr[0]
    elif i == 1 :
        return max(arr[0],arr[1])
    else:
        A = rec_arr(arr,i-2)+arr[i]
        B=rec_arr(arr,i-1)
        print ('i : %d ,A:%d , B:%d'%(i,A,B))
        return max (A,B)
def dp_opt(arr,j):
    opt = (0 for i in range(len (a)))
    print(opt)
    opt[0] = arr[0]
    opt[1] = max (arr[1],arr[0])
    for i in range (2,len(arr)):
        opt[i] = max(opt[i-1],opt[i-2]+arr[i])
    return opt[j]
print (rec_arr(a,6))
print(dp_opt(a,6))
