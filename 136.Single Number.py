'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''
class Solution:
    def singleNumber(self, nums):
        res = []
        for num in nums:
            if num not in res:
                res.append(num)
            else:
                res.remove(num)

        return res[0]

    # solution with bit manipulation
    def singleNumber_2(self, nums):
        res = 0
        for num in nums:
            res ^= num

        return res



#Solution in  Java
# class Solution {
#     public int singleNumber(int[] nums) {
#         List<Integer> list = new ArrayList<>();

#         for(int n : nums){
#             if(list.contains(n)){
#                 list.remove(new Integer(n));
#             }
#             else{
#                 list.add(n);
#             }

#         }
#         return list.get(0);

#     }
# }