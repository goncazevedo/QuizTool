class Option:
	def __init__(self, answer, correct):
		self.answer = answer
		self.correct = correct
		
	def get_answer(self):
		return self.answer

	def get_correct(self):
		return self.correct


	def __str__(self):
 		return "answer: " + answer + " , " + "correct: " + correct
