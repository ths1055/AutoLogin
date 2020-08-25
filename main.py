from lib import b64EnDecode
from lib import info
import selenium
def inputInformation():
    aSite=i.writeSite()
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
while True:
    print("continue? Yes:0 No:1")
    continueOr=int(input(">>>"))
    if continueOr==0:
        inputInformation()
    else:
        break
        

f=open('data.dat','r')
findSite=str(input('Website to find>>>'))
while True:
    passingSite=b.b64Decode(f.readline())
    if findSite==passingSite:
        passingId=b.b64Decode(f.readline())
        passingPw=b.b64Decode(f.readline())
        
        break

print(passingSite)
print(passingId)
print(passingPw)
