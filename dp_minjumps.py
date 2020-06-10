import unittest

def minNumberOfJumps(array):
	# populate array with max upper bound
	jumps = [float('inf') for x in array] 
	# distance from first index to itself is 0
	jumps[0] = 0 
	# iterate through entire array
	for i in range(1, len(array)):
		# iterate from 0 to current index exclusive
		for j in range(0, i):
			# if at or farther than index i
			if array[j] + j >= i: 
				# min # of jumps needed to go from first index to indices 
				jumps[i] = min(jumps[j] + 1, jumps[i])
	return jumps[-1] #return final value in jumps array

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3],4))
	def test_case_2(self):
		self.assertEqual(minNumberOfJumps([1],0))
	def test_case_3(self):
		self.assertEqual(minNumberOfJumps([1, 1],1))
	def test_case_4(self):
		self.assertEqual(minNumberOfJumps([3, 1],1))
	def test_case_4(self):
		self.assertEqual(minNumberOfJumps([2, 1, 1],1))

# Time O(N^2) due to double for loops
# Space O(N) due to jumps array