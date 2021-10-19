class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max = 0
		for i, l in enumerate(s):
			subs = l
			for j, m in enumerate(s):
				if m not in subs:
					subs += m
					size = len(subs)
					if size > max:
						max = size
				else:
					break
		return max

solution = Solution()
max = solution.lengthOfLongestSubstring("abcabcab")
print(max)
