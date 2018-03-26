'''
Created on Mar 25, 2018

@author: sandipsr
'''

def createLists():
    list1 = ['hello', "world", 30998, 30.5, None]
    return list1;

def performListOperation():
    print("performListOperation :--------------------------------START")
    list1 = createLists()
    print(list1[0]);
    print(list1[1:3]);
    print(list1);           
    #print(list1.pop())
    print(list1.remove('hello'))
    print(list1);
    print("performListOperation :--------------------------------END")

def createTuple():
    #tuple1 = {'hello', "world", 30998, 30.5, None}
    tuple1 = {10 , 44 ,22, 444, 22.8,3}
    return tuple1;

def performTupleOperation():
    print("performTupleOperation :--------------------------------START")
    tuple1 = createTuple();
    print(tuple1)
    #print(tuple1[0]);
    for item in tuple1:
        
        print(item*2)
    
    #print(tuple1[1:3])
    
    print(tuple1)
    
    print("performTupleOperation :--------------------------------END")
    
def createDictionary():
    dict1 = {'name': 'john','code':6734, 'dept': 'sales'}
    return dict1


def performDictOperation():
    print("performDictOperation :--------------------------------END")
    dict1 = createDictionary();    
    print(dict1)
    print(dict1['name'])
    print(dict1.keys());
    print(dict1.values());
    print("performDictOperation :--------------------------------END")
    
#performListOperation();
#performTupleOperation();
performDictOperation()



