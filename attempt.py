# https://superfastpython.com/multiprocessing-race-condition-python/
# https://superfastpython.com/thread-race-condition-shared-variable/

# SuperFastPython.com
# example of an attempted race condition with a shared variable
from time import sleep
from multiprocessing import Process
from multiprocessing import set_start_method
values = [1.0]

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
    fuck = float(0)
    for x in range(len(values)):
        fuck = fuck + values[x]
    return fuck*4
 
if __name__ == '__main__':
    # set start method
    set_start_method('spawn')
    # define the global variable
    # start a thread making additions
    producer(1, 10000)
    producer(1001, 2000)
    producer(2001, 3000)
    #producer_thread = Process(target=producer, args=(1, 10000))
    #producer_thread.start()
    print('Waiting for processes to finish...')
    #producer_thread.join()
    # starting total calc
    sum = consumer()
    #consumer_thread = Process(target=consumer)
    #consumer_thread.start()
    #consumer_thread.join()
    # wait for total calc to finish
    # report the value
    print(f'Value: {values[4]}')
    print(f'Value: {sum}')
