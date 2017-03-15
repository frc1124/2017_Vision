
def thingOut(i):
    out = bin(abs(i))[2:].zfill(5)
    print i
    print out
    print '\n'
    print 0 if i>0 else 1 #sign
    print out[4]          #bit one
    print out[3]          #bit two
    print out[2]          #bit three
    print out[1]          #bit four
    print out[0]          #bit five
    return;

#writeOut(-1)

def writeOut
