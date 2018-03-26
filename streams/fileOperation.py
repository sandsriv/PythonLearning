'''
Created on Mar 25, 2018

@author: sandipsr
'''
from array import array
import threading

def openFile(filename, mode="r"):
    fileObject = open(filename, mode)
    print("File Object created with \n name= :{}, \n mode= :{},\n encoding= :{}"
          .format(fileObject.name,
                  fileObject.mode,
                  fileObject.encoding));
    fileObject.tell();              
    return fileObject

def readFileContent(filename, position=0):
    fileObject = openFile(filename)
    print("Filename passed as: {} \n position: {}".format(filename, position))
    return fileObject.read(position)
    
def wordcount(filename):
    #fileContent = readFileContent(filename, 100000);
    #print("FileContent : \n {} ".format(fileContent))
    wordDict1 = {};
    with openFile(filename, "r") as lines:
        for line in lines:
            #print(line)
            #lines_arr.append(line)
            line = line.strip('\n')
            line = line.strip('\t')
            line = line.strip('')
            line = line.split("\\s+")
#             print(line[0])
            
            line_arr = line[0].split(" ")
#             print(line_arr)
            
            
            for pline in line_arr:
#                 print(pline)
                if(pline in wordDict1):  
                    wordDict1[pline] = wordDict1[pline] + 1;
                else:
                    wordDict1[pline] = 1;
                    
    print(threading.activeCount())
                
    for k in wordDict1.keys():
        print(k , wordDict1.get(k) ,"\n")
        
        