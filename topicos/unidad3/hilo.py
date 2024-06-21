import threading
class mithread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
    def run(self):
        print "soy el hilo",self.num
print "soy el hilo princial"
for i in range(0,10):
    t=mithread(i)
    t.start()
    t.join()