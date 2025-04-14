"""
Maze Explorer module that implements automated maze solving (BFS-enhanced).
"""

import time
import pygame
from typing import Tuple, List, Optional
from collections import deque
from .constants import BLUE, WHITE, CELL_SIZE, WINDOW_SIZE

class Explorer:
    def __init__(self, maze, visualize: bool = False):
        self.maze = maze
        self.x, self.y = maze.start_pos
        self.moves = []
        self.start_time = None
        self.end_time = None
        self.visualize = visualize
        self.backtrack_count = 0  # Maintained for compatibility
        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption("Maze Explorer - Automated Solving (BFS)")
            self.clock = pygame.time.Clock()

    def draw_state(self):
        """Draw the current state of the maze and explorer."""
        self.screen.fill(WHITE)
        
        # Draw maze
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                   (x * CELL_SIZE, y * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE))
        
        # Draw start and end points
        pygame.draw.rect(self.screen, (0, 255, 0),
                        (self.maze.start_pos[0] * CELL_SIZE,
                         self.maze.start_pos[1] * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0),
                        (self.maze.end_pos[0] * CELL_SIZE,
                         self.maze.end_pos[1] * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        
        # Draw explorer
        pygame.draw.rect(self.screen, BLUE,
                        (self.x * CELL_SIZE, self.y * CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        
        pygame.display.flip()
        self.clock.tick(30)  # Control visualization speed

    def print_statistics(self, time_taken: float):
        """Print detailed statistics about the exploration."""
        print("\n=== Enhanced Maze Explorer (BFS) ===")
        print(f"Total time taken: {time_taken:.4f} seconds")
        print(f"Number of moves: {len(self.moves)}")
        print("===================================")

    def solve(self) -> Tuple[float, List[Tuple[int, int]]]:
        """
        Solve the maze using Breadth-First Search to find the shortest path.
        Returns the time taken and the list of moves made.
        """
        self.start_time = time.time()

        start = self.maze.start_pos
        end = self.maze.end_pos
        width, height = self.maze.width, self.maze.height
        visited = [[False] * width for _ in range(height)]
        parent = dict()

        queue = deque()
        queue.append(start)
        visited[start[1]][start[0]] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        found = False
        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                found = True
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < width and 0 <= ny < height and 
                    not visited[ny][nx] and self.maze.grid[ny][nx] == 0):
                    visited[ny][nx] = True
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

        if found:
            path = []
            current = end
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            self.moves = path

            if self.visualize:
                for x, y in self.moves:
                    self.x, self.y = x, y
                    self.draw_state()

        self.end_time = time.time()
        time_taken = self.end_time - self.start_time

        self.print_statistics(time_taken)
        return time_taken, self.moves
