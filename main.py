from lib import b64EnDecode*
from lib import info*
f=open(data.dat,r)
if None == f.read(1):
    f.close()
    #이부분에서 input으로 입력받고 info 모듈로 정보 넘겨줄것
    