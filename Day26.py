class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}

        arr2.sort()

        for arr1_val in arr1:
            newDp = collections.defaultdict(lambda: math.inf)

            for val, steps in dp.items():
                if arr1_val > val:
                    newDp[arr1_val] = min(newDp[arr1_val], steps)

                i = bisect_right(arr2, val)
                if i < len(arr2):
                    newDp[arr2[i]] = min(newDp[arr2[i]], steps + 1)

            if not newDp:
                return -1

            dp = newDp

        return min(dp.values())
