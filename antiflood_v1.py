from time import time

flooders = {}
MESSAGES = 3
SECONDS = 1

oldtime = time

def isFlood(userid):

    userid = str(userid)
    
    try:
        flooders[userid].append(time())
    except:
        flooders[userid] = []
        flooders[userid].append(time())
    
    for i in flooders[userid]:
        flooders[userid] = list(filter(lambda x: time()-int(x)<SECONDS, flooders[userid]))
            
        if len(flooders[userid]) > MESSAGES:
            return (True)
        else:
            return (False)

for i in range(300):
    input("")
    if isFlood(11):
        print("flood")
    else:
        print("non flood")
