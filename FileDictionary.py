import os
import sys

class FileDictionary:

	def __init__(self, file_path=None):
		self._words = {}
		self._display_string = 'word'
		if file_path: # if file_path is passed in, populate hashmap
			self.new_file(file_path)

	def tokenize(self, line):
		"""
		Generator function to return tokens to be iterated over.

		:param line: line to be tokenized
		:returns: iterator 
		"""
		for token in line.split():
			yield token

	def new_file(self, file_path):
		"""
		Parses a new file and maps words to their number of occurrences in the 
		hashmap. Stores the result into the _words instance variable

		:param file_path: path to file to be parsed
		:returns: void
		"""
		self._file_path = file_path
		if not os.path.isfile(file_path):
			print('Pleaes Double Check File Path')
			return False
		with open(file_path) as f:
			maxLength = 0
			for line in f:
				for token in self.tokenize(line):
					self._words[token] = self._words.get(token, 0) + 1
					maxLength = max(maxLength, len(token))
			self._display_string += ' ' * (maxLength - 3)
			self._display_string += '|count'

	def get_word_count(self, word=None):
		"""
		Prints count value associated with a word. Displays 0 for words that DNE.
		If the word parameter is not passed in, this function prints counts for 
		all words

		:param word: word to check count for
		:returns: void
		"""
		if word:
			print('{0} : {1}'.format(word, self._words.get(word, 0)))
		else:
			print(self._display_string) # display string for indicating what each column represents
			print('-----------------------')
			for word in self._words:
				print('{0} : {1}'.format(word, self._words[word]))

	def top_k_words(self, k):
		pass


if __name__ == '__main__':
	if len(sys.argv) < 2: 
		print('Incorrect Use')
	else:
		myDict = FileDictionary(sys.argv[1])
		q_string = 'Which word would you like to seek (blank for All words | EXIT to exit program): '
		var = input(q_string)		
		while var != 'EXIT':
			myDict.get_word_count(var)
			var = input(q_string)
		print('Exiting Program. Thank you for using File Dictionary')
