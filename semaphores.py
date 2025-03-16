import multiprocessing
import time
import random

# ConnectionPool class with semaphore for controlled access
class ConnectionPool:
    def __init__(self, max_connections):  # Fixed typo here: __init__ instead of _init_
        self.pool = ["DB_Conn_" + str(i) for i in range(max_connections)]
        self.semaphore = multiprocessing.Semaphore(max_connections)

    def get_connection(self):
        self.semaphore.acquire()
        return self.pool.pop()

    def release_connection(self, connection):
        self.pool.append(connection)
        self.semaphore.release()

# Function simulating database access
def access_database(pool, process_id):
    print(f"Process {process_id} is waiting for a connection...")
    connection = pool.get_connection()
    print(f"Process {process_id} acquired {connection}.")
    
    time.sleep(random.uniform(1, 3))  # Simulate work with the database
    
    pool.release_connection(connection)
    print(f"Process {process_id} released {connection}.")

# Main function to set up multiprocessing
def main():
    max_connections = 3  # Limit the number of connections
    pool = ConnectionPool(max_connections)  # Pass max_connections argument
    processes = []
    num_processes = 6  # More processes than connections

    for i in range(num_processes):
        p = multiprocessing.Process(target=access_database, args=(pool, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
