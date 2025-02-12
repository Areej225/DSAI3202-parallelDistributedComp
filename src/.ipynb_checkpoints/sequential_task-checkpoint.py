import time
from src.functions import calculate_partial_sum

def run_sequential(n):
    """Sequential summation from 1 to n"""
    start_time = time.time()
    result = calculate_partial_sum(1, n)
    end_time = time.time()

    print(f"Sequential Sum: {result}")
    print(f"Execution Time (Sequential): {end_time - start_time} seconds")
