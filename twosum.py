"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the complement and its index
        num_to_index = {}
        
        # Iterate through the array
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = index
        
        # If no solution is found (though the prompt guarantees one)
        raise ValueError("No two sum solution")
