'''
Lastbuild:2020.12.19 16:32:37
**본 코드는 평가의 목적으로만 이용 가능하며 그 이외의 용도로 이용시 저작권법에 의거 처벌받으실 수 있습니다.**
코드히스토리는 https://github.com/ths1055/prconProject/commits/master 에서 확인하실 수 있습니다.
이 코드는 2020.12.18 Chrome브라우저  87.0.4280.88 버전과 Chromedriver 87.0.4280.88버전의 64비트 환경에서 작성되었습니다.
'''
from lib import b64EnDecode
from lib import info
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from tkinter import*
from tkinter import messagebox

a=Tk()
a.geometry('400x100')
a.title('autoLogin')

i=info.checkInfo()
b=b64EnDecode.b64ed()
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

def d_reset():
    response=messagebox.askyesno('초기화 주의!','저장된 모든 데이터를 초기화 하시겠습니까?')
    if response == 1:
        f=open('data.dat','w')
        f.write('')
        f.close()
        messagebox.showinfo('완료','초기화되었습니다.')
    
    elif response == 0:
        messagebox.showinfo('취소','취소되었습니다.')

def find_identi():
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
    if passingSite == 'google':
        googles(passingId,passingPw)

    elif passingSite == 'riroschool':
        riroschool(passingId,passingPw)

    elif passingSite == 'kakaomail':
        kakaomail(passingId,passingPw)
    
#사용 가능한 사이트:카카오 메일, 다음 카카오 로그인, 구글
#사용불가 사이트:리로스쿨(저장된 id,pw만 안내)

Label(a,text='Auto Login').grid(row=1,column=4)
Label(a,text='    ').grid(row=2,column=1)
Button(a,text='ID,PW RECORD',command=inputInformation,width=15).grid(row=2,column=2)
Label(a,text='').grid(row=2,column=3)
Button(a,text='FIND ID,PW',command=find_identi,width=15).grid(row=2,column=4)
Label(a,text='').grid(row=2,column=5)
Button(a,text='DATA RESET',command=d_reset,width=15).grid(row=2,column=6)
messagebox.showwarning('주의','caution.txt파일을 정독한 후 사용해 주십시오')
a.mainloop()