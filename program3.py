class Node:
	def __init__(self, data):
		self.data = data
		self.next = next
	
class LinkedList:
	def __init__(self):
		self.head = None
	
	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	def length_of_longest_substring(self):
		substring = []
		count = 0
		max = 0
		temp = self.head
		while temp:
			if temp.data not in substring:
				substring.append(temp.data)

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		list_str = LinkedList()
		for l in s:
			list_str.push(l)
		return list_str.length_of_longest_substring()

solution = Solution()
length = solution.lengthOfLongestSubstring("abcabcbb")
print(length)
