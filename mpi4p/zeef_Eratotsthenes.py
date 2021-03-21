from mpi4py import MPI

class Sequential:

    def __init__(self, limit):
        self.limit = limit
        self.k = 2
    
    def create_zeef(self):
        self.zeef = {i : 0 for i in range(self.k, self.limit+1)}
    
    def mark_non_prime(self):
        i= self.k**2
        while i <= self.limit:
             self.zeef[i] = 1
             i += self.k

    def find_next_k(self):# set k
        i = self.k
        while i <= self.limit:
            i+=1
            if self.zeef[i] == 0:
                self.k = i 
                break 
    
    def find_prime_numbers(self):
        while self.k**2 <= self.limit:
            self.mark_non_prime()
            self.find_next_k()
    
    def prime_numbers(self):
        return [index for index, number in self.zeef.items() if number == 0]

class Parallel:

    def __init__(self, limit):
        self.limit = limit

    def find_prime_numbers(self):
        comm = MPI.COMM_WORLD
        comm_rank = comm.Get_rank()
        comm_size = comm.Get_size()

        
if __name__ == "__main__":
    
    s = Sequential(1000)
    s.create_zeef()
    s.find_prime_numbers()
    print(len(s.prime_numbers()))
    


    

        



