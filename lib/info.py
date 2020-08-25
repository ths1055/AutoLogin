from lib import b64EnDecode

b6=b64EnDecode.b64ed()
class checkInfo:
    def writeId(self):
        wId=0
        wId=str(input("id>>>"))
        if wId == '':
            a=1
        else:
            wId_after=b6.b64Encode(wId)
            a=0
            f=open('data.dat','a')
            f.write(wId_after)
            f.write('\n')
            f.close()
        return a
    
    def writePw(self):
        wPw=0
        wPw=str(input("pw>>>"))
        if wPw =='':
            b=1
        else:
            b=0
            wPw_after=b6.b64Encode(wPw)
            f=open('data.dat','a')
            f.write(wPw_after)
            f.write('\n')
            f.close()
        return b
