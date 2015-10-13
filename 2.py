##n=leng(a)
from math import sqrt

# in file
fin = open('in8.txt', 'r')
# fout
fout = open('2out1.txt', 'w')
# 2out1.txt
n = 0
a = []
rz = []
for i in fin:
    rz = i.split()
    n = n + 1
    rz[0] = int(rz[0])
    rz[1] = int(rz[1])
    a.append(rz)

#print(a)
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
print('n =', n)

b = [[0]*n for i in range(n)]
bm = [0]*n
mR = 1000**1000
s = []
mcount = [0]*n

import time
millis1 = int(round(time.time() * 1000))

# Massiv s rasstoianiami do centra koordinat
allr = []
for i in range(n):
    ds = []
    ds.append(sqrt((a[i][0]*a[i][0] + a[i][1]*a[i][1])))
    ds.append(i)
    allr.append(ds)
#print(allr)

allr.sort()
'''
for (i, item) in enumerate(allr):
    print(i, item)
'''
# smotrim v masive allr
def getradius(i):
    j = i
    ri = allr[i][1]
    while j < n:
        if j == i:
            j =j +1
            continue
        rj = allr[j][1]

        r = sqrt((a[ri][0]-a[rj][0])**2 + (a[ri][1]-a[rj][1])**2)

        b[ri][rj] = r
        if r < bm[ri]:
            bm[ri] = r

        if allr[j][0] > bm[ri] + allr[i][0]:
            j = n + 1
        j = j + 1

     #   print ( i,j,r,bm)

    j = i
    while j >= 0:
        if j == i:
            j = j -1
            continue
        rj = allr[j][1]

        r = sqrt((a[ri][0]-a[rj][0])**2 + (a[ri][1]-a[rj][1])**2)

        b[ri][rj] = r
        if r < bm[ri]:
            bm[ri] = r

        if allr[j][0] < allr[i][0] - bm[ri]:
            j = 0
         #   print (i ,j ,'ii', allr[j][0], bm[ri], allr[i][0])
        j = j - 1


def gets(i):
    rcount = 0
    ds = [] #tekushie sosedi
    j = i
    ri = allr[i][1]
    while j < n:
        if j == i:
            j= j + 1
            continue
        rj = allr[j][1]
        if b[ri][rj] == 0:
            b[ri][rj] = sqrt((a[ri][0]-a[rj][0])**2 + (a[ri][1]-a[rj][1])**2)

        if 2*bm[ri] >= b[ri][rj]:
            rcount += 1
            print ('b',i ,j,'s','2*bm[ri]',2*bm[ri],' b[ri][rj]', b[ri][rj])

        if allr[j][0] > 2*bm[ri] + allr[i][0]:
            j = n + 1
        j = j + 1

    j = i
    while j >= 0:
        if j == i:
            j = j -1
            continue
        rj = allr[j][1]

        if b[ri][rj] == 0:
            b[ri][rj] = sqrt((a[ri][0]-a[rj][0])**2 + (a[ri][1]-a[rj][1])**2)

        if 2*bm[ri] >= b[ri][rj]:
            rcount += 1
            print ('m',ri ,rj,'s','2*bm[ri]',2*bm[ri],' b[ri][rj]', b[ri][rj])

        if allr[j][0] < allr[i][0] - 2*bm[ri]:
            j = 0
        j = j - 1

    mcount[ri] = rcount

for i in range(n):
    bm[i] = mR

for i in range(n):
    getradius(i)

for i in range(n):
    gets(i)

for i in range(n):
    ri = allr[i][1]
    r = bm[i]
    fout.write(str((r)) + ' ' + format(mcount[i])+'\n')

'''
print(a)
print(b)
print(bm)
print(mcount)
'''

millis2 = int(round(time.time() * 1000))
tm = (millis2-millis1)/1000
print("time =", tm, "s")
fout.write('time2 = '+format(tm))

