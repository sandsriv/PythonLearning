'''
Created on Mar 25, 2018

@author: sandipsr
'''
from random import random

class PrintJob(object):
    '''
    classdocs
    '''

    def __init__(self, jobPrefix, type="default", name="default"):
        '''
        Constructor
        '''
        self.id   = jobPrefix +'_'+ str(random())
        self.type = type;
        self.name = name
        
    def printJobDetails(self):
        _msg = "JOB Details \n ID: {}, \n TYPE:{} \n NAME:{}"
        return (_msg.format(self.id, self.type, self.name))
     