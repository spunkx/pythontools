import time

accTime = 0
aTime = []
for i in range(0,600):
    #avoiding error propagation
    currmilTime = time.time() * 1000
    filePointer = open(str(i)+".txt","w+")
    filePointer.write("testdfsdfsdfsdfdf" + str(i))
    nextmilTime = time.time() * 1000
    timeTaken = nextmilTime - currmilTime
    aTime.append(timeTaken)
    accTime = accTime + timeTaken

print("operation took", str(accTime)+"ms")
print("average time was", str(accTime/i)+"ms")
