import unittest
import homework_week3_Kara_Howard

characters1 = "cbacba"
phrase1 = "aabbccc"

characters2 = "leHd ol!Wrlo"
phrase2 = "Hello World!"

characters3 = "leHdol!Wrlo"
phrase3 = "Hello World!"

class TestFile(unittest.TestCase):
	def test_generate_phrase(self):
		self.assertEqual(homework_week3_Kara_Howard.generate_phrase(characters1, phrase1), False)
		self.assertEqual(homework_week3_Kara_Howard.generate_phrase(characters2, phrase2), True)
		self.assertEqual(homework_week3_Kara_Howard.generate_phrase(characters3, phrase3), False)

if __name__ == '__main__':
	unittest.main()