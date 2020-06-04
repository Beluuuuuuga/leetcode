class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        half = len(costs) / 2
        
        sum = []
        min_val = 0
        for i, v in enumerate(costs):
            tmp = v[1] - v[0]
            sum.append([i,tmp])
            

        sum.sort(key=lambda x: x[1], reverse=True)
        
        for i in range(n):
            tmp = sum[i][0]
            if i < half:
                min_val += costs[tmp][0]
            else:
                min_val += costs[tmp][1]
                
        return min_val
