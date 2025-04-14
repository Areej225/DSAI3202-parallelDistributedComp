from multiprocessing import Pool
from src.maze import create_maze
from src.explorer import Explorer
import pandas as pd

def run_bfs_explorer(index):
    maze = create_maze(width=None, height=None, maze_type="static")
  # or "static"
    explorer = Explorer(maze)
    time_taken, moves = explorer.solve()
    return {
        "Explorer": f"BFS Explorer {index}",
        "Maze Type": "Static",
        "Moves": len(moves),
        "Time (s)": round(time_taken, 4),
        "Start": maze.start_pos,
        "End": maze.end_pos
    }

def main():
    num_explorers = 6  # You can change this number
    with Pool(processes=num_explorers) as pool:
        results = pool.map(run_bfs_explorer, range(1, num_explorers + 1))

    df = pd.DataFrame(results)
    print("\n=== Parallel BFS Explorer Results ===")
    print(df.sort_values("Moves"))

    # Save results
    df.to_csv("parallel_bfs_results.csv", index=False)
    print("\nResults saved to parallel_bfs_results.csv")

if __name__ == "__main__":
    main()
