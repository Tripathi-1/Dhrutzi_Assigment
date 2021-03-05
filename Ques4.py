'''Question 4:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
 
Example 2:
Input: [4,1,2,1,2]
Output: 4
'''
def search(arr, n) :

	XOR = 0
	for i in range(n) :
		XOR = XOR ^ arr[i]

	print("The required element is", XOR)


arr = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]
Len = len(arr)

search(arr, Len)


