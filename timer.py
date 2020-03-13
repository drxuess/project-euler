import time

s = time.time()

def end():
    return "%f seconds" % (time.time() - s)
    
