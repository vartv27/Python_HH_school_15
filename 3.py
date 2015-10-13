
fin = open('in3.txt', 'r')
fout = open('out3.txt', 'w')

def fnd1(s):
    ls =len(s)
    i=0
    f=0
    d=0
    while i < ls-1:
        if int(s[i])+1!=int(s[i+1]) and d==0 and int(s[i])!=9:
     #       print('stop si',s[i],'i',i)
            f=1
        if (d==1):
             if i+2==ls:
                bs = int(s[i-1:i+1])+1
         #       print ('bs',bs)
         #       print(s[i+1])
                if s[i+1]!=str(bs)[0]:
                    f=1
           #         print('bs<>si+1]',str(bs)[0],s[i+1])
             else:
          #      print('ne 11n ','s[i+1:i+3]',s[i+1:i+3],s[i-1:i+1] )
                if int(s[i+1:i+3])!=int(s[i-1:i+1])+1:
                    f=1
         #           print('ne 11n ','i',i,'ls',ls,'s[i+1:i+3]',s[i+1:i+3],s[i-1:i+1] )

        if (s[i]=='9') and d==0:
            d=1
            dper = i
            if i+2==ls:
                if s[i+1]!='1':
                    f=1
#                    print('ne1 odin1 el si+1',s[i+1])
            else:
                if s[i+1:i+3]!='10':
                    f=1
#                    print('ne deset',s[i+1:i+3])
 #                   print('i',i,'ls',ls)
                    i=i-1
        if d==0:
            i+=1
        else:
            i+=2
    return f


def fnd3(s,n):
    global kansw
    global ch9
    ls =len(s)
    i=0
    f=0
    answ=0
    kansw=0

    ch9 =0

    step ='1'   # 10 100 1000 10000
    for i in range(1,n+1):
        step=step+'0'
    answresult=0
    for k in range(n):
        if s[k]=='0':
            continue
        dn = 0
        ns = int(s[k:n+k])+1
      #  ns = int(str(ns)[0:n])  #1000 =>100
        if str(ns)==str(step):
            dn=1

    #    print('step=',str(step),ns);
        ns = str(ns)[0:len(s[k+n:k+2*n+dn])]
        nspo = s[k+n:k+2*n+dn]

    #    print('nss',ns,'s2=',nspo,'n',n,'k',k,'answ',answ)
        if str(ns) == str(nspo) or (k+n>ls):
     #       print ('k raven',k)
            do = s[0:k]
            dosr = int(s[k:n+k])-1 #sravnenie chisel do nachala povtorenii 57 1258 99 1200

            if s[k:n+k]+'0'==str(step):
                ch9 = 1
        #        print ('cheee')

            if len(str(dosr)) == n:
                dosr = str(dosr)[n-k:n]
            else:
                dosr = str(dosr)[n-k-1:n-1]

            if n+k>ls:
                do= s[k:ls]+s[k-(n+k-ls):k]
                dosr=s[k:n]+s[0:k]
    #            print ('etot n+l>ls')

     #       print('do', do,'dosr', str(dosr), 'n', n, 'k', k, 'ls', ls)
            if str(do) == str(dosr):
                f=1

                i=k+n
                while i+1 <= ls-n:
                    ns = int(s[i:i+n+dn])+1
                    ns = int(str(ns)[0:n+dn])  #1000 =>100
                    ns = str(ns)[0:len(s[i+n+dn:i+2*(n+dn)])]
                #    print(ns,'s2=',s[i+n:i+2*n])
                #    ns = int(s[i:i+n+dn])

                    if ns!=s[i+n+dn:i+2*(n+dn)]:
                        f=0
            #            print('break', ns,'s2=',s[i+n+dn:i+2*(n+dn)], 'k=', k, 'i', i,'len', len(s[i+n+dn:i+2*(n+dn)]),'dn', dn)
                        break
            #        print('no break ns =', ns,'s2=',s[i+n+dn:i+2*(n+dn)],'k',k,'i',i,'len',len(s[i+n+dn:i+2*(n+dn)]))

                    if str(ns) == str(step[0:len(step)]):
                        dn=1
                        i=i-dn
                    i=i+n+dn

                if f == 1:
                    answ = int(s[k:n+k])-1
                    if k == 0:
                         answ = str(s[k:n+k])
                    if n+k > ls:
                        answ = str(do)

                    if answresult == 0:
                        answresult = answ
                        kansw = k
                    if int(answ) < int(answresult):
                        answresult = answ
                        kansw = k
                #        if kansw ==4:
                   #         print('dsad')

  #  print('answresult', answresult, 'kansw',kansw)
    return answresult

#s='5715815'
#s='23456712345681234567'
#n=4 23 51235 2      51 2352
#s='5512355' #n=4     23551 23552
#s='845238' #n=5
#s='8765487' #n=5
#s='99101'

def schet(s,k):
    rez=0
    s=str(s)
    ls=len(s)
    if ls==1:
        return s
    step='1'
    for i in range(1,ls):
        step=step+'0'
    rez=int(s)-int(step)
    rez= rez*ls+10
    i=2
    while i<ls:
        rez=rez+9*(10**(i-1))*i
        i+=1

    rez=rez+k
    return rez


def rez(s):
    s=str(s)
    kd=0
    mx = len(str(s))
    global kansw
    kansw=0

    rezult = 0
    fn=fnd1(s)
    if fn == 0:
        rezult = s[0]
    else:
       fl=0

       for d9 in range(len(s)):
           if s[d9]!='9':
               fl=1
       if fl==0 :
           return  schet(s,0)
       n=2

       while n<=mx:
           ff = fnd3(s,n)
           if ff:
                dbk = n - kansw - ch9
                if kansw==0:
                    dbk=0
                rezult = schet(ff,dbk)
          #      print ( 'rz',ff,dbk,n)
                break
           n=n+1
    return rezult

#print ('dd',fnd3('90004',5))

''' Proverka do schet ( oknchatelnoho rescgeta
ms= ['101','10','21','92','921','991','9100','123124','123125', '125123', '31241','910001','9991001','4321','99992','99999','998999','001','93456','934561',
     '1000110002','999100010011002','8999100010','991000100','9100010011002','1100210','5676','1234567124']
mso= ['10','10','12','29','192','99' ,'99'  ,'123'   ,'123125', '123125' , '123',    '999' ,'1001999','1432','29999','99999','998','100','34569','193456',
      '10001','999','998','999','999','1001','675','4567123']
k=0
for k in range(len(ms)):
    print('n=',ms[k],' o=' , mso[k],'rez=', rez(ms[k]))
    a2=1
'''

m = [[1, 1],
      [2, 2],
      [23, 2],
    [9, 9],
    [6789, 6],
     [111, 12],
     [101, 10],
     [21, 15],
     [99, 188],
     [91001, 189],
     ['0101', 192],
     [9989991, 2884],
     [10011002, 2894],
     ['0011002', 2895],
     ['011002', 2896],
     [11002, 2897],
     [5789, 22046],
     [8957, 22048],
     [8579, 1626],
     ]

for i in range(len(m)):
    a11=0
#    print(m[i][0], m[i][1], rez(m[i][0]))

for i in fin:
    fout.write(str(rez(int(i)))+'\n')



