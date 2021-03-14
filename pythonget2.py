import requests as req
import threading as thr
import time
import json
from random import seed
from random import random
seed()
userlist=['username1','username2','username3','username4','username5']
test_start=time.ctime()
timer_s=time.perf_counter()

class stressthread(thr.Thread):
    def __init__(self,threadID,name):
        thr.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=1
    def run(self):
        test_start=time.ctime()
        if(self.threadID==1):
            f=open('Thread1.txt','a')
        elif(self.threadID==2):
            f=open('Thread2.txt','a')
        elif(self.threadID==3):
            f=open('Thread3.txt','a')
        elif(self.threadID==4):
            f=open('Thread4.txt','a')
        elif(self.threadID==5):
            f=open('Thread5.txt','a')
        elif(self.threadID==6):
            f=open('Thread6.txt','a')
        elif(self.threadID==7):
            f=open('Thread7.txt','a')
        elif(self.threadID==8):
            f=open('Thread8.txt','a')
        elif(self.threadID==9):
            f=open('Thread9.txt','a')
        elif(self.threadID==10):
            f=open('Thread10.txt','a')
        #print(f'Starting {self.name}')
        f.write(f'\nTEST FROM: {test_start}\n')
        url=''
        count=0
        urlint=0
        while count<=100:
            url='https://www.webpage.com/login?u='
            #print(f'{self.name} REQUEST #{count}')
            f.write(f'REQUEST #{count+1}\n')
            urlint=int(random()*10%5)
            if urlint==1:
                url=url+userlist[1]
                #print('USER: USERNAME2')
                f.write('USER: USERNAME2\n')
            elif urlint==2:
                url=url+userlist[2]
                #print('USER: USERNAME3')
                f.write('USER: USERNAME3\n')
            elif urlint==3:
                url=url+userlist[3]
                #print('USER: USERNAME4')
                f.write('USER: USERNAME4\n')
            elif urlint==4:
                url=url+userlist[4]
                #print('USER: USERNAME5')
                f.write('USER: USERNAME5\n')
            else:
                url=url+userlist[0]
                #print('USER: USERNAME1')
                f.write('USER: USERNAME1\n')
            starttime=time.perf_counter()
            r=req.get(url)
            endtime=time.perf_counter()
            #print(f'STATUS CODE: {r.status_code}')
            f.write(f'STATUS CODE: {r.status_code}\n')
            #print(f'RESPONSE TIME: {endtime-starttime:0.4f} seconds')
            f.write(f'RESPONSE TIME: {endtime-starttime:0.4f} seconds\n\n')
            #print()
            json_stress(r.json(), self, urlint)
            count+=1
        f.close()
        #print(f'Exiting {self.name}')
#print('Defined stressthread class')

def server_stress():
    thread1=stressthread(1,'Thread1')
    thread2=stressthread(2,'Thread2')
    thread3=stressthread(3,'Thread3')
    thread4=stressthread(4,'Thread4')
    thread5=stressthread(5,'Thread5')
    thread6=stressthread(6,'Thread6')
    thread7=stressthread(7,'Thread7')
    thread8=stressthread(8,'Thread8')
    thread9=stressthread(9,'Thread9')
    thread10=stressthread(10,'Thread10')
    
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
#print('Defined server_stress() function')

def json_stress(js, thrd, uint):
    if(thrd.threadID==1):
        m=open('thr1MP3.txt','a')
    elif(thrd.threadID==2):
        m=open('thr2MP3.txt','a')
    elif(thrd.threadID==3):
        m=open('thr3MP3.txt','a')
    elif(thrd.threadID==4):
        m=open('thr4MP3.txt','a')
    elif(thrd.threadID==5):
        m=open('thr5MP3.txt','a')
    elif(thrd.threadID==6):
        m=open('thr6MP3.txt','a')
    elif(thrd.threadID==7):
        m=open('thr7MP3.txt','a')
    elif(thrd.threadID==8):
        m=open('thr8MP3.txt','a')
    elif(thrd.threadID==9):
        m=open('thr9MP3.txt','a')
    elif(thrd.threadID==10):
        m=open('thr10MP3.txt','a')
    timetotal=0
    loopnum=0
    m.write(f'Thread{thrd.threadID} login: {thrd.counter}\nTest from: {test_start}\nUser: {userlist[uint]}\n')
    for item in js:
            if (item.get('Location','')!=''):
                try:
                    start=time.perf_counter()
                    r2=req.get(item['Location'])
                    end=time.perf_counter()
                    it=item['Location']
                    thistime=end-start
                    m.write(f'{it} responded in {thistime:0.4f} seconds\n')
                    timetotal+=thistime
                #print('check')
                except Exception as ex:
                    m.write(f'Exception in thread {thrd.name}\nException message: {ex}\n')
                    print(f'Exception in thread {thrd.name} with exception message: {ex}\n')
            loopnum+=1
    timeavg=timetotal/loopnum
    m.write(f'AVERAGE TIME: {timeavg:0.4f}\n')
    m.write(f'TOTAL TIME: {timetotal:0.4f}\n\n')
    m.close()
    thrd.counter+=1
    #print('done')
#print('Defined json_stress() function')

print(f'TEST FROM: {test_start}')
try:
    server_stress()
except:
    print('Something went wrong...')
else:
    timer_e=time.perf_counter()
    print(f'Test completed in {(timer_e-timer_s)} seconds')
