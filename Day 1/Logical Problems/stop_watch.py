import time

def stopwatch():
    input("Press Enter to Start time: ")
    start_time = time.time()
    
    input("Press Enter to End Time: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Elapsed Time:{elapsed_time:.2f} seconds")
    
stopwatch()    