'''
Created on Mar 25, 2018

@author: sandipsr
'''
import datetime
import threading
import time
from threading import Condition


class PrintServer(object):
    '''
    classdocs
    '''
    jobList1 = [];
    #threadLock = threading.Lock()
    threadLock = threading.Lock()
    

    def __init__(self, resource):
        '''        Constructor         '''
        global jobList1;
        self.resource = resource;
        self.jobList  = []
        self.condition  = Condition();
        
    def executJob(self, job):
        #self.threadLock.acquire()
        print("|--------------------- PRINTER EXECUTION :START---------------------------|")
        
        print("Executing_job_for_Thread : {}  started @: {}", job.type, datetime.datetime.now())
        
        print("Executing the JOB :-> ", job.printJobDetails())
        time.sleep(5);
        
        print("Executing_job_for_Thread : {}  Finished @: {}", job.type, datetime.datetime.now())
        
        
        print("|--------------------- PRINTER EXECUTION :END-----------------------------|")
        #self.threadLock.release()   

    def addJob(self, job):
        print("|--------------------- ADD JOB :START-------------------------------------|\n")
        print("New Job been added -> ", job.printJobDetails())
        
        self.jobList.append(job);
        
        print("Job Queue Length: now ", self.jobQueueLength())
        print("|--------------------- ADD JOB :ENDT -------------------------------------|")

        
    def removeJob(self, job):
        print("|--------------------- REMOVE JOB :START ---------------------------------|")
        print("Existing Job being removed -> ", job.printJobDetails())
        
        print("Job Queue Length: before ", self.jobQueueLength())
        self.jobList.remove(job)
        print("Job Queue Length: after ", self.jobQueueLength())
        print("|--------------------- REMOVE JOB :END -----------------------------------|")

        
    def jobQueueLength(self):
        return len(self.jobList);
    
    def getLatestJob(self):
        
        return self.jobList[0]; 
        
        