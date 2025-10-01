class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {
            1: (0, 1),  # right
            2: (0, -1), # left
            3: (1, 0),  # down
            4: (-1, 0)  # up
        }
        pq = [(0, 0, 0)]
        cost =[[(float('inf'))] * n for _ in range(m)]
        cost [0][0] = 0
        while pq:
            c, r , c2 = heapq.heappop(pq) 
            if r == m - 1 and c2 == n - 1:
                return c
            current_dir = grid[r][c2]
            dr, dc = directions[current_dir]
            new_r, new_c = r + dr, c2 + dc
            if 0 <= new_r < m and 0 <= new_c < n:
                if c < cost[new_r][new_c]:
                    cost[new_r][new_c] = c
                    heapq.heappush(pq, (c, new_r, new_c))
            for new_dir, (dr, dc) in directions.items():
                new_r, new_c = r + dr, c2 + dc
                if 0 <= new_r < m and 0 <= new_c < n:
                    if new_dir != current_dir:
                        new_cost = c + 1
                        if new_cost < cost[new_r][new_c]:
                            cost[new_r][new_c] = new_cost
                            heapq.heappush(pq, (new_cost, new_r, new_c))
    
        return 0