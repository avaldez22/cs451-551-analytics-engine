#Adrian Valdez 
#Dr Medina 
#CS451 Sft. Engr.

import unittest
from avaldezhw3 import Student_Grades



class TestWrapper(unittest.TestCase):

	def test_init(self):
		a = Student_Grades('/data/grade-data.json')

	def test_avg_grade(self):
		a = Student_Grades('/data/grade-data.json')
		self.assertEqual(a.avg_grade(), 'B')


	def test_grade_change(self):
		a = Student_Grades('/data/grade-data.json')
		self.assertEqual(a.grade_change(), 3.75)


	def test_female_count(self):
		a = Student_Grades('/data/grade-data.json')
		self.assertEqual(a.female_count(), 17)


	def test_male_count(self):
		a = Student_Grades('/data/grade-data.json')
		self.assertEqual(a.male_count(), 72)	
