class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            hr = 0
            i=0
            while i<len(piles):
                hr += int(piles[i]/ mid)
                if piles[i] % mid != 0:
                    hr += 1
                i+=1

            if hr <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans