'''
Created on Mar 25, 2018

@author: sandipsr
'''
from process.thread.NetworkThread import NetworkThread
from process.thread.PrintServer import PrintServer
from process.thread.PrintServerThread import PrintServerThread
import traceback
from process.thread.OperatorThread import OperatorThread

def runNetworkServiceJobOnly():
    PS  = PrintServer("Print-Server:");
    NWS = NetworkThread(1 , "NET-SVC", PS);
    PST = PrintServerThread(2,"PRT-SVC", PS)
    OPT = OperatorThread(3,"OPT-SVC", PS)
    
    try:
        OPT.start();
        print("Started the OPT Thread")
        
        PST.start();
        print("Started the PST Thread")
        
        NWS.start();
        print("Started the NWS Thread")
        
    except Exception as err:
        print("Error in starting thread")
        traceback.print_exception()
        traceback.print_tb(err.__traceback__)
        


runNetworkServiceJobOnly();