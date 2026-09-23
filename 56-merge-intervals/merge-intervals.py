class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            merge_last = res[-1][1]
            if start<= merge_last:
                res[-1][1]= max(merge_last , end)
            else:
                res.append([start,end])
        return res
            

        


