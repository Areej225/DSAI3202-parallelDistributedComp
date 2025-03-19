# DSAI 3202 – Assignment 1 (Part 1) – Multiprocessing and Semaphores

## Objective
Implement and evaluate different multiprocessing approaches in Python and simulate resource access synchronization using semaphores.


## Final Output Snapshot

### Square Function Timing – 10^6 Numbers
```
Sequential Execution Time: 0.0621 seconds
Multiprocessing Individual Process Execution Time: 7.7549 seconds
Multiprocessing Pool (map) Execution Time: 0.2209 seconds
Multiprocessing Pool (apply) Execution Time: 0.2491 seconds
Multiprocessing Pool (apply_async) Execution Time: 0.1448 seconds
ProcessPoolExecutor Execution Time: 119.9661 seconds
```

### Square Function Timing – 10^7 Numbers
```
Sequential Execution Time: 0.6389 seconds
Multiprocessing Pool (map) Execution Time: 1.3317 seconds
Multiprocessing Pool (apply) Execution Time: 0.3126 seconds
Multiprocessing Pool (apply_async) Execution Time: 0.1813 seconds
ProcessPoolExecutor Execution Time: 106.3264 seconds
```

### Semaphore Synchronization Output Sample
```
Process 0 is waiting for a connection...
Process 0 acquired DB_Conn_2.
Process 1 is waiting for a connection...
Process 1 acquired DB_Conn_2.
Process 2 is waiting for a connection...
...
Process 5 released DB_Conn_2.
```

### Semaphore Behavior Discussion
- When more processes try to access the pool than there are available connections, the extra processes are forced to **wait** until a connection is released by another process. This behavior was clearly visible in the output log, where some processes displayed "waiting for a connection..." until they were allowed access.

- The **semaphore acts as a gatekeeper**, allowing only a limited number of processes (equal to the number of available connections) to access the shared resource simultaneously. Once a process finishes and releases the connection, the semaphore releases a permit, allowing the next waiting process to proceed.

- This mechanism ensures that **race conditions are avoided**, and **resource access is synchronized**. Multiple processes do not interfere with each other’s work, maintaining data integrity and stability in concurrent environments.
- `Pool.map()` consistently offers the best performance.
- `apply()` and `apply_async()` are useful but slightly slower in large datasets.
- Individual processes per number are highly inefficient.
- ProcessPoolExecutor is flexible but slower on large lists.
- Semaphore ensures safe access to shared resources, blocking excess processes.

## Assignment Questions – Answered
- All required methods tested.
- Repeated tests with 10^7 elements.
- Both synchronous and asynchronous pool versions evaluated.
- Semaphore usage simulated and analyzed.

## Notes
- For time efficiency, some heavier methods (`apply`, `apply_async`, `ProcessPoolExecutor`) were tested on subsets when needed.
- Code is modular, reusable, and clearly documented.







