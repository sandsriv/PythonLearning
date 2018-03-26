'''
Created on Mar 25, 2018

@author: sandipsr
'''
import streams.fileOperation as fo;

filename = "/home/sandipsr/Software/Spark/spark-2.3.0-bin-hadoop2.7/README.md"
filename1="/home/sandipsr/Documents/LinuxPractice/testfile4"; 
#fo.readFile(filename);
fo.wordcount(filename1)