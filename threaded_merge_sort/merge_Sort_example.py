import threading
import logging
#Bron https://www.youtube.com/watch?v=mc4BtkJ86Ww
class MergeSort(threading.Thread):

    def __init__(self,array: [int], begin: int, end: int):
        threading.Thread.__init__(self)
        self.begin = begin # start of the arr
        self.end   = end # end of the array
        self.array = array  # list to be sorted 
        
    
    def run(self):
        #print that the thread is starting 
        logging.info("Thread is starting between %s and %s", self.begin, self.end)
        if self.begin != self.end: # is this a one list?
            begin_ = self.begin 
            end_   = int((self.begin + self.end)/2)
            begin__= end_ + 1
            end__  = self.end
        
            # print(begin_)
            # print(end_)
            # print(begin__)
            # print(end__)

            left = MergeSort(self.array, begin_, end_)
            right =MergeSort(self.array, begin__, end__)
            left.start()
            right.start()

            left.join()
            right.join()

            #then merge , we can't merge until the 2 threads above are done
            # once this return , we know that left and right arrays are sorted

            temp = []#0 for i in range(self.end - self.begin +1)]
            pos1 = begin_
            pos2 = begin__

            for i in range(self.end - self.begin +1):
                if (pos1 <= end_) and (pos2 <= end__):
                    if (self.array[pos1]) < self.array[pos2]:
                        temp.append(self.array[pos1])
                        pos1+=1
                    else:
                        temp.append(self.array[pos2])
                        pos2+=1
                elif pos1 <= end_:
                    temp.append(self.array[pos1])
                    pos1+=1
                else:
                    temp.append(self.array[pos2])
                    pos2+=1
           
            
            for tempPos in range(len(temp)):
                self.array[tempPos+ self.begin] = temp[tempPos] 
                
            #print(self.array)
        
                






