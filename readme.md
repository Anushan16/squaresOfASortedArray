977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


=====================================================================

For my initial apprach , I squared the given numbers array initially and then called a merge sort funtion. I later found that this method did not account for duplicates abs value elements ie (-3 and 3). Furthermore, the algo was inefficent. I then realilzed the exact value is irelevant and only the abs value matters as -3  ^2 and 3^2 are both 9 , so I utilized Pythons built in sort method, passing in a key of abs for the absolute value. I then used list comprehension to return a new list squaring each element in the sorted array. 