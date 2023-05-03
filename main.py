import time, sys
from parser import readArgs
from consumer import createConsumer, getMessages
from concurrent import startThread
 



#TODO Catch CTRL-C 
def main():
    msgPartition, locationPartition = readArgs()

    messageConsumer = createConsumer("messages", msgPartition)
    locationConsumer = createConsumer("device-location", locationPartition)

    startThread(getMessages, messageConsumer)
    startThread(getMessages, locationConsumer)
    try:
        while True: 
            time.sleep(1)
    except KeyboardInterrupt:
        print ("Shuting Down")
        sys.exit() 


main()
