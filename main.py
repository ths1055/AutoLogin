from lib import b64EnDecode
from lib import info

def inputInformation():
    while True:
        if aSite==1:
            aId=i.writeSite()
        else:
            break
    aId=i.writeId()
    while True:
        if aId==1:
            aId=i.writeId()
        else:
            break
        
    aPw=i.writePw()
    while True:
        if aPw==1:
            aPw=i.writePw()
        else:
            break

b=b64EnDecode.b64ed()
i=info.checkInfo()
f=open('data.dat','r')
if '' == f.read(1):
    f.close()
    #이부분에서 input으로 입력받고 info 모듈로 정보 넘겨줄것
    inputInformation()


f=open('data.dat','r')
while True:
    