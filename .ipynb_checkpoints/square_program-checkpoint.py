import multiprocessing
import concurrent.futures
import time
import random

# Function to compute square of a number
def square(num):
    return num * num

# Generate a list of 10^6 random numbers
NUMBERS_1M = [random.randint(1, 1000) for _ in range(10**6)]
NUMBERS_10M = [random.randint(1, 1000) for _ in range(10**7)]

# Sequential Execution
def sequential_squares(numbers):
    start = time.time()
    results = [square(num) for num in numbers]
    end = time.time()
    print(f"Sequential Execution Time: {end - start:.4f} seconds")
    return results

# Multiprocessing with a process for each number
def multiprocessing_squares(numbers):
    start = time.time()
    processes = []
    results = []

    def collect_result(result):
        results.append(result)

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        for num in numbers:
            pool.apply_async(square, args=(num,), callback=collect_result)
        pool.close()
        pool.join()
    
    end = time.time()
    print(f"Multiprocessing Execution Time: {end - start:.4f} seconds")
    return results

# Using Pool.map
def multiprocessing_pool_map(numbers):
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    end = time.time()
    print(f"Multiprocessing Pool (map) Execution Time: {end - start:.4f} seconds")
    return results

# Using Pool.apply
def multiprocessing_pool_apply(numbers):
    start = time.time()
    results = []
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        for num in numbers:
            results.append(pool.apply(square, args=(num,)))
    end = time.time()
    print(f"Multiprocessing Pool (apply) Execution Time: {end - start:.4f} seconds")
    return results

# Using concurrent.futures ProcessPoolExecutor
def process_pool_executor(numbers):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(square, numbers))
    end = time.time()
    print(f"ProcessPoolExecutor Execution Time: {end - start:.4f} seconds")
    return results

# Running Tests for 10^6 numbers
print("Running tests for 10^6 numbers:")
sequential_squares(NUMBERS_1M)
multiprocessing_squares(NUMBERS_1M)
multiprocessing_pool_map(NUMBERS_1M)
multiprocessing_pool_apply(NUMBERS_1M)
process_pool_executor(NUMBERS_1M)

# Running Tests for 10^7 numbers
print("\nRunning tests for 10^7 numbers:")
sequential_squares(NUMBERS_10M)
multiprocessing_squares(NUMBERS_10M)
multiprocessing_pool_map(NUMBERS_10M)
multiprocessing_pool_apply(NUMBERS_10M)
process_pool_executor(NUMBERS_10M)