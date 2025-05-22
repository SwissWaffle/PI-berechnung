# https://superfastpython.com/multiprocessing-race-condition-python/
# https://superfastpython.com/thread-race-condition-shared-variable/

# SuperFastPython.com
# example of an attempted race condition with a shared variable
import threading
import time
import math
values = [1.0]
sum = 0

# erstellt brüche zwischen 1/range_min und 1/range_max
def producer(range_min, range_max):
    global values
    k = range_min
    for i in range(range_min, range_max):
        values.append((-1 if (i%2) else +1)/((2*k)+1))
        k = k+1
    return
 
# zusammer zähler der brüche
def consumer():
    global values
    global sum
    for x in range(len(values)):
        sum = sum + values[x]
    sum = sum*4
    return
 
if __name__ == '__main__':
    # start a thread making additions
    producer1_thread =threading.Thread(target=producer, args=(1, 1000))
    producer2_thread =threading.Thread(target=producer, args=(1001, 2000))
    #starting threads
    producer1_thread.start()
    producer2_thread.start()
    
    print('Waiting for processes to finish...')
    
    producer1_thread.join()
    producer2_thread.join()
    # starting total calc
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    consumer_thread.join()
    # wait for total calc to finish
    #report the value
    #print(f'Value: {values[4]}')
    rel_error = 100*((math.pi-sum)/sum)
    diff= sum-math.pi
    print(f'Value = {sum}')
    print(f'Pi = {math.pi}')
    print(f'Diff to Pi = {diff}')
    print(f'rel_error ={rel_error:^ .10f}%')