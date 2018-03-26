'''
Created on Mar 25, 2018

@author: sandipsr
'''
import datetime
import threading
import time
import traceback

from process.thread.PrintServer import PrintServer
from process.thread.data.PrintJob import PrintJob


MAX_JOB_QUEUE_LENGTH = 1;
condition = None;

class NetworkThread(threading.Thread):
    ''' classdocs '''
    threadLock = threading.Lock()
    
    RUN_NETWORK_THREAD_ENABLED = True
    
    def __init__(self, svcid,svcname, PS):
        '''         Constructor  '''
        threading.Thread.__init__(self)
        global RUN_NETWORK_THREAD_ENABLED;
        self.id   = svcid;
        self.name = svcname;
        self.printserver = PS
        
    # --------------------------------------------------------------------------------------
    #
    # Thread __submitJob method:
    # This method submits all NetworkRelated Jobs to the resource PrintServer for execution.
    # If the queue is full, it waits for notification from other threads.
    # --------------------------------------------------------------------------------------
        
    def __submitJob(self, job):
        condition = self.printserver.condition;
        condition.acquire()
        print("NetworkThread acquires the Lock @ :{}", datetime.datetime.now())
        
        while(self.printserver.jobQueueLength() >= MAX_JOB_QUEUE_LENGTH):
            
            print("NetworkThread waits as PrintServer Resource is busy. @: {}", datetime.datetime.now())
            condition.wait();
            
            print("NetworkThread receives notification now. @: {}", datetime.datetime.now())
        
        print("NetworkThread sending job @ :{}", datetime.datetime.now())
        self.printserver.addJob(job)
        condition.notify();
        condition.release();
        print("NetworkThread releasing the Lock @ :{}", datetime.datetime.now())

    # --------------------------------------------------------------------------------------
    #
    # Thread run method
    #
    # --------------------------------------------------------------------------------------
    def run(self):
        i = 0;
        while(True):
            try:
                job = PrintJob("Network:", "Network", (i+1))
                self.__submitJob(job)
                
                time.sleep(5)
                i= i+1;
            except Exception as err:
                print('Exception while running NetworkThread thread')
                traceback.print_exception()
                traceback.print_tb(err.__traceback__)
                
                