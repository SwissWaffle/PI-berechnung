# https://superfastpython.com/multiprocessing-race-condition-python/
# https://superfastpython.com/thread-race-condition-shared-variable/

# SuperFastPython.com
# example of an attempted race condition with a shared variable
import threading
import time
import math
values = [0.0]
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
    # var nr_of_threads ändern zur gewünschten thread anzahl, darf nicht <=0 sein
    nr_of_threads = 8
    for n in range(nr_of_threads):
        #erstellung der threads 
        if(n==0):
            exec('producer'+str(n)+'_thread = threading.Thread(target=producer, args=(1, 1000))')
        else:
            exec('producer'+str(n)+'_thread = threading.Thread(target=producer, args=('+str((n*1000)+n)+', '+str(((n+1)*1000)+n)+'))')
        
    #starting threads
    for n in range(nr_of_threads):
        exec('producer'+str(n)+'_thread.start()')
    
    print('Waiting for processes to finish...')
    
    for n in range(nr_of_threads):
        exec('producer'+str(n)+'_thread.join()')
        
    # starting total calc
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    consumer_thread.join()
    # wait for total calc to finish
    #report the value
    #print(f'Value: {values[4]}')
    rel_error = 100*((math.pi-sum)/sum)
    diff= sum-math.pi
    print(f'Nr of Threads = {nr_of_threads}')
    print(f'Value = {sum}')
    print(f'Anzahl Werte = {len(values)}')
    print(f'Pi = {math.pi}')
    print(f'Diff to Pi = {diff}')
    print(f'rel_error ={rel_error:^ .10f}%')