'''
Created on Mar 25, 2018

@author: sandipsr
'''
import datetime
import threading
import time
import traceback

from process.thread.data.PrintJob import PrintJob


MAX_JOB_QUEUE_LENGTH = 1;
class OperatorThread(threading.Thread):
    '''     classdocs     '''

    def __init__(self, svcid,svcname, PS):
        '''         Constructor  '''
        threading.Thread.__init__(self)
        global RUN_NETWORK_THREAD_ENABLED;
        self.id   = svcid;
        self.name = svcname;
        self.printserver = PS
    
    # --------------------------------------------------------------------------------------
    #
    # Thread __submitJob method
    #
    # --------------------------------------------------------------------------------------
    
    def __submitJob(self, job):
        condition = self.printserver.condition;
        condition.acquire();
        print("OperatorThread acquires the Lock @ :{}", datetime.datetime.now())
        
        while(self.printserver.jobQueueLength() >= MAX_JOB_QUEUE_LENGTH):
            
            print("OperatorThread waits as PrintServer Resource is busy. @: {}", datetime.datetime.now())
            condition.wait();
            
            print("OperatorThread receives notification now. @: {}", datetime.datetime.now())
        
        print("OperatorThread sending job @ :{}", datetime.datetime.now())
        self.printserver.addJob(job)
        condition.notify();
        condition.release();
        print("OperatorThread releasing the Lock @ :{}", datetime.datetime.now())
    
    # --------------------------------------------------------------------------------------
    #
    # Thread run method
    #
    # --------------------------------------------------------------------------------------
    def run(self):
        i = 0;
        while(True):
            try:
                job = PrintJob("Operator:", "Operator", (i+1))
                self.__submitJob(job)
                
                time.sleep(2)
                i= i+1;
            except Exception as err:
                print('Exception while running OperatorThread')
                traceback.print_exception()
                traceback.print_tb(err.__traceback__)               