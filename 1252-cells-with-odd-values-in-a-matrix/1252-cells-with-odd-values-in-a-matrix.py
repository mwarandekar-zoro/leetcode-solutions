class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Step 1: Record how many times each row & column is hit
        for r, c in indices:
            row_counts[r] += 1
            col_counts[c] += 1
            
        # Step 2: Check each cell's parity
        odd_count = 0
        for r in range(m):
            for c in range(n):
                if (row_counts[r] + col_counts[c]) % 2 != 0:
                    odd_count += 1
                    
        return odd_count