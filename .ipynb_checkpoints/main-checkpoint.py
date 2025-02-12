from src.sequential_task import run_sequential
from src.threads_task import run_threads
from src.processes_task import run_processes

N = 10**7  # Define the range

if __name__ == "__main__":
    print("Running Sequential Execution:")
    run_sequential(N)

    print("\nRunning Threaded Execution:")
    run_threads(N, num_threads=4)

    print("\nRunning Multiprocessing Execution:")
    run_processes(N, num_processes=4)
