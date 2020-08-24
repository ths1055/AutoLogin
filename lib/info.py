class checkInfo:
    def writeId(self):
        wId=0
        wId=str(input("id>>>"))
        if wId == '':
            a=1
        else:
            a=0
            f=open('temp.tmp','a')
            f.write(wId)
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
            f=open('temp.tmp','a')
            f.write(wPw)
            f.write('\n')
            f.close()
        return b
