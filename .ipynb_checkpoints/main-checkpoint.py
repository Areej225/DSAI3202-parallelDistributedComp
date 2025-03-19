from src.square_program import run_square_tests
from src.semaphores import run_semaphore_simulation

def main():
    print("========== Running Part 1: Square Function Tests ==========")
    run_square_tests()

    print("\n========== Running Part 1: Semaphore Simulation ==========")
    run_semaphore_simulation()

if __name__ == "__main__":
    main()
