
# Every blocking I/O call in the standard library releases the GIL therefore Python threads are excellent 
# for I/O-bound systems. The concurrenct.futures pkg has threadpool that's easy to use, as shown below.


from concurrent import futures

MAX_THREADS = 4

rslts = []

# simplest way to run several callables concurrently is with the Executor.map function

with futures.ThreadPoolExecutor(MAX_THREADS) as exctr:
    # results returned by executor.map is a generator
    # implicitly, the __next__ method of the results generator must wait until the first future is complete
    # 
    # print could be executed in random order as each print takes unknown time as an IO bound operation
    rslts = exctr.map(lambda x: print(f"result: {x}"), range(1, 10))  

# Executor.map function is easy to use but it has a feature that may or may not be helpful,
# depending on your needs: it returns the results exactly in the same order as the calls are 
# started: if the first call takes 10s to produce a result, and the others take 1s each, 
# your code will block for 10s as it tries to retrieve the first result of the generator 
# returned by map. 
# 
# Often it’s preferable to get the results as they are ready, regardless of the order they were submitted. 
# To do that, you need a combination of the Executor.submit method and the futures.as_completed function

print('### submit and as_complete example below ###')

to_dos = []

with futures.ThreadPoolExecutor(MAX_THREADS) as exctr2:
    for i in range(10, 20):
        to_dos.append(exctr2.submit(lambda x: x * 10, i))

print('to do jobs are submitted in parallel')

for future in futures.as_completed(to_dos):  # results are collected when each is done thus in random order
    print(f"result: {future.result()}")




