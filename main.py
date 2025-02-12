from src.sequential_task import run_sequential
from src.threads_task import run_threads
from src.processes_task import run_processes
import time

def performance_analysis():
    num_threads = 4  
    num_processes = 4  
    P = 0.9  # Assume 90% of the task is parallelizable

    # Measure execution times
    print("\nRunning Sequential Execution...")
    start = time.time()
    run_sequential(10**7)  # Using 10 million as input
    T_sequential = time.time() - start

    print("\nRunning Threading Execution...")
    start = time.time()
    run_threads(10**7, num_threads)
    T_threads = time.time() - start

    print("\nRunning Multiprocessing Execution...")
    start = time.time()
    run_processes(10**7, num_processes)
    T_processes = time.time() - start

    # Compute Speedups
    S_threads = T_sequential / T_threads
    S_processes = T_sequential / T_processes

    # Compute Efficiencies
    E_threads = S_threads / num_threads
    E_processes = S_processes / num_processes

    # Compute Amdahl’s Speedup
    S_A_threads = 1 / ((1 - P) + (P / num_threads))
    S_A_processes = 1 / ((1 - P) + (P / num_processes))

    # Compute Gustafson’s Speedup
    S_G_threads = (1 - P) + (P * num_threads)
    S_G_processes = (1 - P) + (P * num_processes)

    # Print results
    print("\n=== Performance Analysis Results ===")
    print(f"Sequential Time: {T_sequential:.6f} sec")
    print(f"Threading Time: {T_threads:.6f} sec, Speedup: {S_threads:.2f}, Efficiency: {E_threads:.2f}")
    print(f"Multiprocessing Time: {T_processes:.6f} sec, Speedup: {S_processes:.2f}, Efficiency: {E_processes:.2f}")
    print(f"Amdahl’s Law Speedup (Threads): {S_A_threads:.2f}")
    print(f"Amdahl’s Law Speedup (Processes): {S_A_processes:.2f}")
    print(f"Gustafson’s Law Speedup (Threads): {S_G_threads:.2f}")
    print(f"Gustafson’s Law Speedup (Processes): {S_G_processes:.2f}")

# Running tasks in order to match lab output
print("task 3_a: sequential")
run_sequential(10**7)

print("\ntask 3_b: Parallelize with Threading")
run_threads(10**7, 4)

print("\ntask 3_c: Parallelize with Multiprocessing")
run_processes(10**7, 4)

print("\ntask 3_d: Performance analysis")
performance_analysis()
