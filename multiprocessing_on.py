import multiprocessing
import sys
import time

sys.path.append('/home/sungmin/dev/src/coding_examples/multiprocessing_test')
from worker_functions import worker_random_max, worker_division

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please specify the number of execution.'
        sys.exit(1)

    start = time.time()

    # # Create processes and start
    # processes = []
    # for i in range(int(sys.argv[1])):
    #     processes.append(multiprocessing.Process(target=worker_random_max))
    #     processes[-1].start()
    # # Wait for the processes to complete
    # for p in processes:
    #     p.join()

    # Create a Pool object
    pool = multiprocessing.Pool()
    # Execute in paraller
    results = []
    for i in range(int(sys.argv[1])):
        results.append(pool.apply_async(worker_random_max, []))
    # And get the result
    for r in results:
        r.get()

    end = time.time()

    print 'multiprocessing_on : %s seconds took' % (end - start)
