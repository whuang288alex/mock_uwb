import mock_uwb
import datetime
import time

time.sleep(5)

for i in range(100):
    
    a = datetime.datetime.now()
    diff = mock_uwb.main()
    b = datetime.datetime.now()
    
    print("\nnumber {i} round, average diff across 100 tests: {diff}".format(i=i+1, diff=diff))
    print("total time spent: {i} seconds".format(i= (b-a).total_seconds()))


