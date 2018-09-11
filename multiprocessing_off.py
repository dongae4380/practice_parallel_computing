import sys
import time

sys.path.append('/home/sungmin/dev/src/coding_examples/multiprocessing_test')
from worker_functions import worker_random_max, worker_division

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please specify the number of execution.'
        sys.exit(1)

    START = time.time()
    for i in range(int(sys.argv[1])):
        worker_random_max()
    END = time.time()

    print 'multiprocessing_off : %s seconds took' % (END - START)
