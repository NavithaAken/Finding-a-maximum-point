def max_points(nums):
    if not nums:
        return 0

    # Count occurrences of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Initialize dynamic programming table
    dp = [0] * (max(nums) + 1)
    dp[1] = count.get(1, 0)

    # Fill the dynamic programming table
    for num in range(2, max(nums) + 1):
        dp[num] = max(dp[num - 1], dp[num - 2] + count.get(num, 0) * num)

    return dp[max(nums)]

# Example usage
nums = [3, 4, 2, 2, 3, 4, 2]
print("Maximum points:", max_points(nums))
