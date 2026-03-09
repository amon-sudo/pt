m = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(m)
res = [1]*n

for i in range(n):
    for j in range(i):
        if m[i] > m[j]:
           res[i] = max(res[i], res[j]+1)
           

print(max(res))



v = [5, 3, 4, 8, 7]

s = len(v)

p = [i] * s

for i in range(s):
    for j in range(i):
        if p[i] < p[j]:

            
            
            
