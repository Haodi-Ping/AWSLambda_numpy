import numpy
import time

def testfunctions(event, context):

    import datetime
    tm_st = datetime.datetime.now()
    for i in range(1):
        for j in range(1):
            for k in range(2):
                s = numpy.array([[i, j, k], [k, j, i]])
                print(s)
   
# testfunctions()

