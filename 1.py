##n=leng(a)

fo = open('in8.txt', 'r')
n = 0
a = []
rz = []
for i in fo:
    rz = i.split()
    n = n + 1
    rz[0] = int(rz[0])
    rz[1] = int(rz[1])
    a.append(rz)
#print(a)
print('n =', n)
'''
n = 5
dx = 2
dy = n
a = [[0 for x in range(dx)] for y in range(dy)]
matrix = [[0 for x in range(dx)] for y in range(dy)]
for i in range(n):
    a[i][0] = i
    a[i][1] = i*i
print(a)
'''
b = [[0]*n for i in range(n)]
bm = [0]*n
mR = 1000**1000
s = []
mcount = [0]*n

import time
millis1 = int(round(time.time() * 1000))

def getradius(i):
    j = 0
    while j < n:
        if j == i:
            j =j +1
            continue
        r = (a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2
        b[i][j] = r
        if r < bm[i]:
            mj = j
            bm[i] = r
     #   print('i', i, 'j', j,r)
        j=j+1

def gets(i):
    r2 = 4 * bm[i]
    rcount = 0
    ds = [] #tekushie sosedi
    for k in range(n):
        if k == i:
            continue
        #print (r2,'i',i,'b[i][k]',b[i][k])

        if r2 >= b[i][k]:
            ds.append(k)
            rcount += 1
        #   print ('sss',r2,'i',i,'b[i][k]',b[i][k])
    mcount[i] = rcount
    s.append(ds) #vse sosedi

for i in range(n):
    bm[i] = mR
    getradius(i)
    gets(i)

from math import sqrt
f = open('out1.txt', 'w')
for i in range(n):
    r = sqrt(bm[i])
    f.write(str((r))+' '+format(mcount[i])+'\n')

'''
n = 1000
fr = open('in9.txt', 'w')
maxx = 1000
import random
for i in range(n):
    x = random.randint(0, maxx)
    y = random.randint(0, maxx)
    #f.write(format(a[0][i])+' '+format(a[1][i])+'\n')
    fr.write(format(x)+' '+format(y)+'\n')


print(s)
print(a)
print(b)
print(bm)
print(mcount)
'''

millis2 = int(round(time.time() * 1000))
tm = (millis2-millis1)/1000
print("time =", tm, "s")
f.write('time = '+format(tm))

