import mock_uwb
import datetime
import time

for i in range(100):
    
    start_time = datetime.datetime.now()
    diff = mock_uwb.main(err = 25, show_debug = True, testing = True)
    end_time = datetime.datetime.now()
    
    print("\nnumber {i} round, average diff across 100 tests: {diff}".format( i = i + 1, diff = diff))
    print("total time spent: {i} seconds".format( i = (end_time - start_time).total_seconds()))


