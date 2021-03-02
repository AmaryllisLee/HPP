# Computes an approximation of Pi by summing up
# a series of terms.  The more terms, the closer
# the approximation.
# Based on a variation of the Gregory-Leibniz series approximation
#
import threading

def f( x ):
    """
    The function being integrated, and which returns
    an approximation of Pi when summed up over an interval
    of integers.
    """
    return 4.0 / ( 1 + x*x )

class WorkerThread(threading.Thread):
    
    def __init__(self, args):
        """
        args must contain n1, n2, and deltaX, in that order.
        """
        threading.Thread.__init__(self, args=args)
        self.n1 = args[0] # define the start value of batch
        self.n2 = args[1] # defin end of batch 
        #print(str(self.n1) + "-" + str(self.n2) + "\n")
        self.deltaX = args[2] # define interval
        self.sum = 0
    
    def run(self ):
        """
        This will be called automatically by start() in
        main.  It's the method that does all the work.
        """
        for i in range(self.n1, self.n2 + 1):
            self.sum += f( i * self.deltaX )
        
    def get(self):
        """
        gets the computed sum.
        """
        return self.sum 

def main():
    """
    Gets a number of terms from the user, then sums
    up the series and prints the resulting sum, which
    should approximate Pi.
    """

    # get the number of terms
    N = int( input( "> " ) )

    sum = 0.0          # where we sum up the individual
                       # intervals
    deltaX = 1.0 / N   # the interval

    # sum over N terms
    # for i in range( N ):
    #     sum += f( i * deltaX )

    # sum over N terms wordt nu:
    # itereer over N terms in batches van batch_size
    # maak een worker aan met de respectievelijke batch en laat die summen over N terms (dus in de worker)
    # start je worker
    # voeg toe aan een lijst van workers
    # < 10 regels code
    workers = []
    batch_size = 1000
    for n in range(1 ,N, batch_size): 
        wt = WorkerThread(args = [n,min(n+ batch_size - 1, N),deltaX])
        workers.append(wt)
        wt.start()

    # Itereer over je workers en zorg dat alle data bij elkaar komt. (< 5 regels code)
    for wt in workers: 
        wt.join()
        sum += wt.get()
    
    #3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 ...
    #   3.1415916535  89629 55139
    # 3.1415916535  897929 7622
     #3.1415916535 8961978143
    #3.14159235358978297622472519

    # display results
    print( "sum = %1.20f" % ( sum * deltaX ) )

main()