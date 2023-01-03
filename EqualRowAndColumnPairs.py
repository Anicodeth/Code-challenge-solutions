from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_dict=defaultdict(list)
        for rows in grid:
            for index, number in enumerate(rows):
                col_dict[index].append(number)
                
        col_list=list(col_dict.values())
        pairs=0
        no_of_values=len(col_list)
        for index_rows in range(no_of_values):
            for index_cols in range(no_of_values):
                if col_list[index_cols]==grid[index_rows]:
                    pairs+=1
        return pairs
