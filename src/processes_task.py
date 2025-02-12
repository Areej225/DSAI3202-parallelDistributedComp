import multiprocessing
import time
from src.functions import calculate_partial_sum

def process_worker(start, end, queue):
    """Process worker to compute partial sum"""
    queue.put(calculate_partial_sum(start, end))

def run_processes(n, num_processes=4):
    """Run summation using multiprocessing"""
    chunk_size = n // num_processes
    processes = []
    queue = multiprocessing.Queue()

    start_time = time.time()
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else n
        process = multiprocessing.Process(target=process_worker, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = [queue.get() for _ in range(num_processes)]
    total_sum = sum(results)
    end_time = time.time()

    print(f"Multiprocessing Sum: {total_sum}")
    print(f"Execution Time (Multiprocessing): {end_time - start_time} seconds")
