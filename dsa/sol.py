from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()  # Sort the array in ascending order
        n = len(arr)
        
        # Set the first element to 1
        arr[0] = 1
        
        # Iterate through the array and ensure the absolute difference condition
        for i in range(1, n):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        
        return arr[-1]  # Return the maximum element in the modified array

# Example usage:
solution = Solution()
print(solution.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))  # Output: 2
print(solution.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]))   # Output: 3
print(solution.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]))    # Output: 5
