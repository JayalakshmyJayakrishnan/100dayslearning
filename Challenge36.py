class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n  # Initialize result array

    # Compute prefix products directly into result array
    prefix = 1
    for i in range(n):
      result[i] = prefix
      prefix *= nums[i]  # Update prefix for next index

    # Compute suffix products on the fly and multiply with result
    suffix = 1
    for i in reversed(range(n)):
      result[i] *= suffix
      suffix *= nums[i]  # Update suffix for next index

    return result
