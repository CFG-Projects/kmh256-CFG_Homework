import unittest
import homework_week4_Kara_Howard

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target1 = 44
target2 = 444
target3 = 1004
target4 = 1
target5 = 111
target6 = 1005

class TestFile(unittest.TestCase):

	# Test for first function
	def test_search_in_matrix(self):
		response1 = 'The target is at position [3, 3] in the matrix.'
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix(matrix, target1), response1)
		response2 = [-1, -1]
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix(matrix, target2), response2)
		response3 = 'The target is at position [4, 5] in the matrix.'
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix(matrix, target3), response3)
	
	# Test for second function
	def test_search_in_matrix2(self):
		response4 = 'The target is at position [0, 0] in the matrix.'
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix2(matrix, target4), response4)
		response5 = [-1, -1]
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix2(matrix, target5), response5)
		response6 = [-1, -1]
		self.assertEqual(homework_week4_Kara_Howard.search_in_matrix2(matrix, target6), response6)

if __name__ == '__main__':
	unittest.main()