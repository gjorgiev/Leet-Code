from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def print_linked_list(node):
	#base case
	if node == None:
		return
	# lets print the current node
	print(node.val)
	# print the next nodes
	print_linked_list(node.next)

def construct_number(node):
	num = 0
	while node:
		tmp_num = num
		digit = node.val
		while tmp_num >= 1:
			tmp_num /= 10
			digit *= 10
		num += digit
		node = node.next
	return num

l1 = ListNode(1, ListNode(0, ListNode(9)))
l2 = ListNode(5, ListNode(7, ListNode(8)))
a = construct_number(l1)
b = construct_number(l2)
c = a + b
print(f"a = {a}, b = {b}, c = {c}")

def construct_list(num):
	node = ListNode(num % 10)
	num //= 10
	while num > 0:
		new_node = ListNode(num % 10)
		new_node.next = node
		node = new_node
		num //= 10
	return node

c_node = construct_list(c)
print_linked_list(c_node)

def reverse_list(node):
	prev = None
	current = node
	while (current is not None):
		next = current.next
		current.next = prev
		prev = current
		current = next
	node = prev
	return node

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		a = construct_number(l1)
		b = construct_number(l2)
		c = a + b
		return reverse_list(construct_list(c))
