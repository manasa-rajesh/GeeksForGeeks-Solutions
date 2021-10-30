class Solution:
	def least_average(self, nums, k):
		# Code here
		if k == 0:
		    return 
		if k == 1:
		    return nums.index(min(nums))+1
		curr = 0
		ans = 0
		for i in range(k):
		    curr += nums[i]
		mini = curr
		for i in range(k, len(nums)):
		    curr += nums[i] - nums[i-k]
		    if curr < mini:
		        mini = curr
		        ans = i-k+1
		return ans+1