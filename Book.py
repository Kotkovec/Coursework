class Book:
	def __init__(self):
		self.__title = ""
		self.__authors = 0
		self.__isbn = 0
		self.__type = ""
		self.__pages = 0
		self.__year = 0

	def __str__(self):
		return self.__title

	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, value):
		if(not value.isdigit()):
			self.__title = value

	@property
	def authors(self):
		return self.__authors

	@authors.setter
	def authors(self,value):
		if(type(value) == str):
			self.__authors = value

	@property
	def isbn(self):
		return self.__isbn

	@isbn.setter
	def isbn(self,value):
		if(str(value).isdigit() and value > 0):
			self.__isbn = int(value)

	@property
	def type(self):
		return self.__type

	@type.setter
	def type(self,value):
		if(value.isalpha()):
			self.__type = value

	@property
	def pages(self):
		return self.__pages

	@pages.setter
	def pages(self,value):
		if(str(value).isdigit() and value > 0):
			self.__pages = int(value)

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		if(str(value).isdigit() and value > 0):
			self.__year = int(value)



