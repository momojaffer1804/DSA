class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x , y = len(grid) , len(grid[0])
        arr = []
        for num in grid:
            arr.extend(num)
        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]
        res = []
        index = 0
        for i in range(x):
            row =[]
            for j in range(y):
                row.append(arr[index])
                index+=1
            res.append(row)
        return res
        