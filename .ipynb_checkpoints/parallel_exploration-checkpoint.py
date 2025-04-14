import multiprocessing
from src.maze import StaticMaze
from src.explorer import Explorer

def run_explorer(index):
    maze = StaticMaze(None, None)  # StaticMaze ignores width/height
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()
    return {
        'Explorer': f'Explorer {index}',
        'Time (s)': round(time_taken, 4),
        'Moves': len(moves),
        'Backtracks': explorer.backtrack_count
    }

def main():
    num_explorers = 4  # You can increase this number
    with multiprocessing.Pool(processes=num_explorers) as pool:
        results = pool.map(run_explorer, range(1, num_explorers + 1))

    print("\n=== Parallel Explorer Results ===")
    for res in results:
        print(f"{res['Explorer']}: Time = {res['Time (s)']}s, "
              f"Moves = {res['Moves']}, Backtracks = {res['Backtracks']}")
    
    # Optional: Save to CSV or visualize using pandas
    try:
        import pandas as pd
        df = pd.DataFrame(results)
        df.to_csv("explorer_results.csv", index=False)
        print("\nResults saved to explorer_results.csv")
    except ImportError:
        print("\nInstall pandas to enable CSV export")

if __name__ == "__main__":
    main()
