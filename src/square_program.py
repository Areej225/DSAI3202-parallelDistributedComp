import multiprocessing
import concurrent.futures
import time
import random

# Function to compute square of a number
def square(num):
    return num * num

# Generate a list of 10^6 and 10^7 random numbers
NUMBERS_1M = [random.randint(1, 1000) for _ in range(10**6)]
NUMBERS_10M = [random.randint(1, 1000) for _ in range(10**7)]

# Sequential Execution
def sequential_squares(numbers):
    start = time.time()
    results = [square(num) for num in numbers]
    end = time.time()
    print(f"Sequential Execution Time: {end - start:.4f} seconds")
    return results

# Multiprocessing for loop (process per number) — DEMO ONLY for small data (1000 elements max)
def multiprocessing_individual_process(numbers):
    start = time.time()
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    print(f"Multiprocessing Individual Process Execution Time: {end - start:.4f} seconds")

# Using Pool.map (Best performance)
def multiprocessing_pool_map(numbers):
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    end = time.time()
    print(f"Multiprocessing Pool (map) Execution Time: {end - start:.4f} seconds")
    return results

# Using Pool.apply()
def multiprocessing_pool_apply(numbers):
    start = time.time()
    results = []
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        for num in numbers:
            results.append(pool.apply(square, args=(num,)))
    end = time.time()
    print(f"Multiprocessing Pool (apply) Execution Time: {end - start:.4f} seconds")
    return results

# Using Pool.apply_async() (Asynchronous version)
def multiprocessing_pool_apply_async(numbers):
    start = time.time()
    results = []
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        async_results = [pool.apply_async(square, args=(num,)) for num in numbers]
        for r in async_results:
            results.append(r.get())
    end = time.time()
    print(f"Multiprocessing Pool (apply_async) Execution Time: {end - start:.4f} seconds")
    return results

# Using concurrent.futures ProcessPoolExecutor
def process_pool_executor(numbers):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(square, numbers))
    end = time.time()
    print(f"ProcessPoolExecutor Execution Time: {end - start:.4f} seconds")
    return results

# Main test runner
def run_square_tests():
    print("Running tests for 10^6 numbers:")
    sequential_squares(NUMBERS_1M)
    multiprocessing_individual_process(NUMBERS_1M[:1000])  # Only first 1000 to avoid freeze
    multiprocessing_pool_map(NUMBERS_1M)
    multiprocessing_pool_apply(NUMBERS_1M[:1000])  # Demo small data for timing
    multiprocessing_pool_apply_async(NUMBERS_1M[:1000])  # Demo small data for timing
    process_pool_executor(NUMBERS_1M)

    print("\nRunning tests for 10^7 numbers:")
    sequential_squares(NUMBERS_10M)
    multiprocessing_pool_map(NUMBERS_10M)
# Multiprocessing individual process is intentionally skipped due to inefficiency
    multiprocessing_pool_apply(NUMBERS_10M[:1000])  # Applied only for small sample
    multiprocessing_pool_apply_async(NUMBERS_10M[:1000])  # Applied only for small sample
# Optionally skip this line if timing too slow on your system
    process_pool_executor(NUMBERS_10M[:1000000])  # Limit to 1M items for runtime optimization


if __name__ == "__main__":
    run_square_tests()
