import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):

        counts = Counter(tasks)

        # Max Heap (negative frequencies)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # (remaining_count, available_time)

        while max_heap or queue:
            time += 1

            # Execute most frequent available task
            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count < 0:
                    queue.append((count, time + n))

            # Cooldown complete?
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time