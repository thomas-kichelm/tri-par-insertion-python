import time

a=[120,1,50,45]
start=time.perf_counter()
def tri_inser(a):
    for i in range(1,len(a)):
        var_aux=a[i]
        j=i-1
        while var_aux<a[j] and j>-1 :
            a[j+1]=a[j]
            j-=1

        a[j+1]=var_aux
tps=time.perf_counter()-start
print(a)
print(tps)
