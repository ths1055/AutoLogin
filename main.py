from lib import b64EnDecode
from lib import info

b=b64EnDecode.b64ed()
i=info.checkInfo()
f=open('data.dat','r')
if '' == f.read(1):
    f.close()
    #이부분에서 input으로 입력받고 info 모듈로 정보 넘겨줄것
    aId=i.writeId()
    if aId==1:
        while (aId != 1):
            aId=i.writeId()
        
    aPw=i.writePw()
    if aPw==1:
        while (aPw != 1):
            aPw=i.writeId()
    
    

'''
d=b64EnDecode.b64ed()
a='fsr2103'
c=d.b64Encode(a)
print(c)
'''
