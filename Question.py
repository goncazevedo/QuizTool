class Question:
	def __init__(self, title, dificulty, options):
		self.title = title
		self.dificulty = dificulty
		self.options = options

		
	def get_title(self):
		return self.title

	def get_dificulty(self):
		return self.dificulty

	def get_options(self):
		return self.options



	def __str__(self):
 		return "title: " + self.title + " , " + "dificulty: " + self.dificulty
