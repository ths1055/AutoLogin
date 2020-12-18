from lib import b64EnDecode
from lib import info
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

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

def googles(id_g,pw_g):
    driver=webdriver.Chrome()
    google='https://accounts.google.com/ServiceLogin/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fwebhp%3Fauthuser%3D0&ec=GAVAAQ&flowName=GlifWebSignIn&flowEntry=AddSession'
    driver.get(google)
    driver.find_element_by_name('identifier').send_keys(id_g)
    driver.find_element_by_name("identifier").send_keys(Keys.ENTER)
    time.sleep(10)
    driver.find_element_by_name('password').send_keys(pw_g)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)

def riroschool(id_r,pw_r):
    driver=webdriver.Chrome()
    riroschool='https://gyeongsanhs.riroschool.kr/'
    driver.get(riroschool)
    time.sleep(3)
    driver.find_element_by_name('mid').send_keys(id_r)
    driver.find_element_by_name('mpass').send_keys(pw_r)

def kakaomail(id_r,pw_r):
    driver=webdriver.Chrome()
    kakaomail='https://mail.kakao.com'
    driver.get(kakaomail)
    driver.find_element_by_id('id_email_2').send_keys(id_r)
    driver.find_element_by_id('id_password_3').send_keys(pw_r)
    time.sleep(100)
    

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
#사용 가능한 사이트:카카오 메일, 다음 카카오 로그인, 구글
#사용불가 사이트:리로스쿨
daum_kakao='https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F'
google='https://accounts.google.com/ServiceLogin/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fwebhp%3Fauthuser%3D0&ec=GAVAAQ&flowName=GlifWebSignIn&flowEntry=AddSession'
daum='https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'

if passingSite == 'google':
    googles(passingId,passingPw)

elif passingSite == 'riroschool':
    riroschool(passingId,passingPw)

elif passingSite == 'kakaomail':
    kakaomail(passingId,passingPw)
