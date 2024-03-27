class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        order = []

        for task in freq:
            order.append([0,task, freq[task]])

        time = 1
        while order:

            if order[0][0] >= time:
                time += 1
                continue
            end, task, count = heapq.heappop(order)

            count -= 1
            time += 1
            if count == 0:
                continue 
            
            heapq.heappush(order, [end + n + 1, task, count])

        return time - 1
            
        
