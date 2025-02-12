import threading
import time
from src.functions import calculate_partial_sum

def thread_worker(start, end, result_list, index):
    """Thread worker to compute partial sum"""
    result_list[index] = calculate_partial_sum(start, end)

def run_threads(n, num_threads=4):
    """Run summation using threads"""
    chunk_size = n // num_threads
    threads = []
    results = [0] * num_threads

    start_time = time.time()
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=thread_worker, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    end_time = time.time()

    print(f"Threaded Sum: {total_sum}")
    print(f"Execution Time (Threads): {end_time - start_time} seconds")
