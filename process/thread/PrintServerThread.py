'''
Created on Mar 25, 2018

@author: sandipsr
'''
import datetime
import threading
import time
import traceback


class PrintServerThread(threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, svcid,resource, ps):
        '''         Constructor         '''
        threading.Thread.__init__(self)
        self.id          = svcid;
        self.resource    = resource;
        self.printserver = ps;
        self.jobCount    = 0;
        
    # --------------------------------------------------------------------------------------
    #
    # Thread run method
    #
    # --------------------------------------------------------------------------------------
     
    def run(self):
        while(True):
            try:
                self.processJob()
            except Exception as err:
                print('Exception while running PrintServerThread', Exception)
                traceback.print_exception()
                traceback.print_tb(err.__traceback__)        
     
    # --------------------------------------------------------------------------------------
    #
    # Thread processJob method:
    # This Thread reads the jobs from the queue and send it to the PrintServer resource for
    # execution.
    #
    # --------------------------------------------------------------------------------------
    
    def processJob(self):
        condition = self.printserver.condition;
        condition.acquire()
        print("PrintServerThread acquires the Lock @ :{}", datetime.datetime.now())
        
        while(self.printserver.jobQueueLength() == 0):
            #time.sleep(5);
            print("PrintServerThread is waiting as no Jobs in queue available now.")
            condition.wait()
            print("PrintServerThread receives notification now. @: {}", datetime.datetime.now())
        
        self.jobCount = self.jobCount + 1;
        print("|********************* PrintServer Thread: PROCESSJOB :START *************|")
        
        print("Picking Job from queue with index: {}.".format(self.jobCount))
        job = self.printserver.getLatestJob();
        print("Job details \n ID: {} \n TYPE: {} \n NAME: {}".format(job.id, job.type, job.name)) 
            
        self.printserver.executJob(job)
        self.printserver.removeJob(job)
        
        condition.notify()
        condition.release()
        print("PrintServerThread releasing the Lock @ :{}", datetime.datetime.now())
        print("|********************* PrintServer Thread: PROCESSJOB :END ***************|")
            
# PJ1 = PrintJob('NW')
# PJ2 = PrintJob('OPR')
# PS1 = PrintServer("Network")
# PS1.printJob(PJ1)
# PS2 = PrintServer("Operation")
# PS2.printJob(PJ2)
