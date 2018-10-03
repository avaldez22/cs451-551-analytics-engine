#Adrian Valdez 
#Dr Medina 
#CS451 Sft. Engr.

import json

class Student_Grades():

	def __init__(self, filename = '/data/grade-data.json'):
		self.data = []
		with open(filename) as f:
		    self.data = json.loads(f.read())
		self.grades = {'A':90, 'B':80, 'C':70, 'D':60, 'F':50}


# Find average final grade #
	def avg_grade(self):
		count = 0
		for i in self.data:
			count = count + self.grades[i[3]]
		avg = int(count/len(self.data))
		for i in self.grades:
			if avg == self.grades[i]:
				return i


# Average grade change from midterm to final #
	def grade_change(self):
		diff = []
		for i in self.data:
			x = self.grades[i[2]]
			y = self.grades[i[3]]
			w = abs(y-x)
			diff.append(w)
		count = 0
		for i in diff:
			count = count + i
		avg = count/len(diff)
		return avg


	#number of female students 
	def female_count(self):
		count = 0
		for i in self.data:
			if i[1] == 'F':
				count = count + 1
		return count

	#Calculates the number of male students 
	def male_count(self):
		count = 0
		for i in self.data:
			if i[1] == 'M':
				count = count + 1
		return count



if __name__ == '__main__':
	#Call all functions
	value = Student_Grades()
	print ()
	print ('The average grade is:', value.avg_grade())
	print ('The average change grade is:', value.grade_change())
	print ('Number of boys:', value.male_count())